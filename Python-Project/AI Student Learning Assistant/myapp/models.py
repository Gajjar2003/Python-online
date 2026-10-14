
from django.db import models
from django.contrib.auth.models import User


class QuizResult(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    topic = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    total_questions = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def percentage(self):
        if self.total_questions == 0:
            return 0

        return round(
            (self.score / self.total_questions) * 100,
            2
        )

    def __str__(self):
        return f"{self.user.username} - {self.topic}"
