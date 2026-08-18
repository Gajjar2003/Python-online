from django import forms
from booking.models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "username",
            "email",
            "mobile",
            "slot_time",
            "duration",
        ]

        widgets = {

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter username"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter email"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter mobile number"
                }
            ),

            "slot_time": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "readonly": True
                }
            ),

            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "readonly": True
                }
            ),
        }