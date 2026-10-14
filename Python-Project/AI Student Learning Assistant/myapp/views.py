
import json
import time

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from google import genai
from google.genai import errors

from myapp.models import QuizResult


# ---------------- LOGIN ----------------

def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "user-login.html")


# ---------------- REGISTER ----------------

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get(
            "confirm_password", ""
        )

        if not username or not email or not password or not confirm_password:
            messages.error(request, "Please fill all fields.")

        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")

        elif len(password) < 8:
            messages.error(
                request,
                "Password must contain at least 8 characters."
            )

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect("user-login")

    return render(request, "register.html")


# ---------------- DASHBOARD ----------------

@login_required(login_url="user-login")
def dashboard(request):
    results = QuizResult.objects.filter(user=request.user)

    total_quizzes = results.count()

    total_questions = sum(
        result.total_questions for result in results
    )

    correct_answers = sum(
        result.score for result in results
    )

    if total_questions > 0:
        overall_percentage = round(
            correct_answers / total_questions * 100, 2
        )
    else:
        overall_percentage = 0

    return render(
        request,
        "dashboard.html",
        {
            "total_quizzes": total_quizzes,
            "overall_percentage": overall_percentage,
        }
    )


# ---------------- LOGOUT ----------------

@login_required(login_url="user-login")
def user_logout(request):
    logout(request)
    return redirect("user-login")


# ---------------- GEMINI ERROR HANDLER ----------------

def show_gemini_error(request, error, feature_name):
    print(f"{feature_name} API Error:", repr(error))

    if getattr(error, "code", None) == 429:
        messages.error(
            request,
            "Gemini API quota exceeded. Please wait until your "
            "quota resets or check your API plan."
        )
    elif getattr(error, "code", None) == 503:
        messages.error(
            request,
            "Gemini AI is temporarily busy. Please try again later."
        )
    else:
        messages.error(
            request,
            f"{feature_name} failed. Check the terminal for details."
        )


# ---------------- AI STUDY CHAT ----------------

@login_required(login_url="user-login")
def ai_chat(request):
    answer = ""

    if request.method == "POST":
        question = request.POST.get("question", "").strip()
        api_key = settings.GEMINI_API_KEY

        if not question:
            messages.error(request, "Please enter your question.")

        elif not api_key:
            messages.error(
                request,
                "API key missing. Check your .env file and settings.py."
            )

        else:
            try:
                client = genai.Client(api_key=api_key)

                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=(
                                "You are a helpful student learning assistant. "
                                "Explain concepts in simple English with examples.\n"
                                "Student question: " + question
                            )
                        )

                        answer = (
                            response.text
                            or "AI returned an empty answer."
                        )
                        break

                    except errors.APIError as error:
                        if (
                            getattr(error, "code", None) == 503
                            and attempt < 2
                        ):
                            time.sleep(2 ** (attempt + 1))
                            continue
                        raise

            except errors.APIError as error:
                show_gemini_error(request, error, "AI Chat")

            except Exception as error:
                print("AI Chat Error:", repr(error))
                messages.error(
                    request,
                    "AI response failed. Please check your API settings."
                )

    return render(
        request,
        "ai-chat.html",
        {"answer": answer}
    )


# ---------------- AI QUIZ GENERATOR ----------------

@login_required(login_url="user-login")
def ai_quiz(request):
    quiz = []
    topic = ""

    if request.method == "POST":
        action = request.POST.get("action", "")

        # Submit quiz
        if action == "submit_quiz" or "submit_quiz" in request.POST:
            quiz = request.session.get("ai_quiz", [])
            topic = request.session.get("ai_quiz_topic", "")

            if not quiz:
                messages.error(
                    request,
                    "Quiz session expired. Please generate a new quiz."
                )
                return redirect("ai-quiz")

            score = 0

            for index, item in enumerate(quiz):
                selected = request.POST.get(
                    f"question_{index}", ""
                )

                if selected == item["answer"]:
                    score += 1

            total = len(quiz)

            QuizResult.objects.create(
                user=request.user,
                topic=topic,
                score=score,
                total_questions=total
            )

            request.session.pop("ai_quiz", None)
            request.session.pop("ai_quiz_topic", None)

            return render(
                request,
                "quiz-result.html",
                {
                    "score": score,
                    "total": total,
                    "topic": topic,
                }
            )

        # Generate quiz
        topic = request.POST.get("topic", "").strip()

        if not topic:
            messages.error(request, "Please enter a quiz topic.")

        elif not settings.GEMINI_API_KEY:
            messages.error(request, "Gemini API key is missing.")

        else:
            try:
                client = genai.Client(
                    api_key=settings.GEMINI_API_KEY
                )

                prompt = f"""
Create 5 multiple-choice quiz questions about: {topic}

Return ONLY a valid JSON array.
Each question must contain these keys:
question, options, answer.

Requirements:
- Exactly 4 options per question.
- The answer must exactly match one option.
- Use simple English.
- Do not include Markdown or explanations outside the JSON.

Example:
[
  {{
    "question": "What is Python?",
    "options": [
      "Programming language",
      "Web browser",
      "Database",
      "Operating system"
    ],
    "answer": "Programming language"
  }}
]
"""

                response = None

                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=prompt
                        )
                        break

                    except errors.APIError as error:
                        if (
                            getattr(error, "code", None) == 503
                            and attempt < 2
                        ):
                            time.sleep(2 ** (attempt + 1))
                            continue
                        raise

                if response is None or not response.text:
                    raise ValueError(
                        "Gemini returned an empty response."
                    )

                response_text = response.text.strip()

                # Remove Markdown code fences if present
                if response_text.startswith("```"):
                    lines = response_text.split("\n")

                    if lines:
                        lines = lines[1:]

                    if lines and lines[-1].strip().startswith("```"):
                        lines = lines[:-1]

                    response_text = "\n".join(lines).strip()

                quiz = json.loads(response_text)

                if not isinstance(quiz, list) or len(quiz) != 5:
                    raise ValueError(
                        "Expected exactly 5 quiz questions."
                    )

                for item in quiz:
                    if not isinstance(item, dict):
                        raise ValueError("Invalid question format.")

                    if not isinstance(item.get("question"), str):
                        raise ValueError("Question text is invalid.")

                    options = item.get("options")
                    answer = item.get("answer")

                    if (
                        not isinstance(options, list)
                        or len(options) != 4
                        or not all(
                            isinstance(option, str)
                            for option in options
                        )
                    ):
                        raise ValueError("Invalid quiz options.")

                    if not isinstance(answer, str) or answer not in options:
                        raise ValueError("Invalid correct answer.")

                request.session["ai_quiz"] = quiz
                request.session["ai_quiz_topic"] = topic

            except errors.APIError as error:
                quiz = []
                show_gemini_error(request, error, "AI Quiz")

            except (ValueError, json.JSONDecodeError) as error:
                print("Quiz Format Error:", repr(error))
                quiz = []
                messages.error(
                    request,
                    "Quiz generation returned an invalid format. "
                    "Please try again."
                )

            except Exception as error:
                print("AI Quiz Error:", repr(error))
                quiz = []
                messages.error(
                    request,
                    "Quiz generation failed. Please try again."
                )

    return render(
        request,
        "ai-quiz.html",
        {
            "quiz": quiz,
            "topic": topic,
        }
    )


# ---------------- SMART NOTES ----------------

@login_required(login_url="user-login")
def ai_notes(request):
    topic = ""
    notes = ""

    if request.method == "POST":
        topic = request.POST.get("topic", "").strip()

        if not topic:
            messages.error(request, "Please enter a topic.")

        elif not settings.GEMINI_API_KEY:
            messages.error(request, "Gemini API key is missing.")

        else:
            try:
                client = genai.Client(
                    api_key=settings.GEMINI_API_KEY
                )

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=f"""
You are StudyMate AI, a student learning assistant.

Create study notes about: {topic}

Use simple English and this format:
1. Topic Introduction
2. Important Concepts
3. Key Points
4. Simple Examples
5. Quick Revision Summary

Make the notes clear and easy to understand.
"""
                )

                notes = response.text or "No notes were generated."

            except errors.APIError as error:
                show_gemini_error(request, error, "Smart Notes")

            except Exception as error:
                print("Smart Notes Error:", repr(error))
                messages.error(
                    request,
                    "Something went wrong while generating notes."
                )

    return render(
        request,
        "ai-notes.html",
        {
            "topic": topic,
            "notes": notes,
        }
    )


# ---------------- LEARNING PROGRESS ----------------

@login_required(login_url="user-login")
def learning_progress(request):
    results = list(
        QuizResult.objects.filter(
            user=request.user
        ).order_by("-created_at")
    )

    total_quizzes = len(results)

    percentages = [
        result.percentage for result in results
    ]

    average_score = (
        round(sum(percentages) / total_quizzes, 2)
        if total_quizzes else 0
    )

    best_percentage = max(percentages, default=0)

    total_questions = sum(
        result.total_questions for result in results
    )

    correct_answers = sum(
        result.score for result in results
    )

    overall_percentage = (
        round(correct_answers / total_questions * 100, 2)
        if total_questions else 0
    )

    return render(
        request,
        "learning-progress.html",
        {
            "results": results,
            "total_quizzes": total_quizzes,
            "average_score": average_score,
            "best_percentage": best_percentage,
            "overall_percentage": overall_percentage,
        }
    )
