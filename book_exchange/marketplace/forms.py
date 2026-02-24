from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "subject",
            "grade",
            "price",
            "is_free",
            "condition",
            "phone_number",
            "image",
            "description"
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Book title"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),
            "grade": forms.Select(attrs={
                "class": "form-select"
            }),
            "condition": forms.Select(attrs={
                "class": "form-select"
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Price"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "WhatsApp number with country code"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Any notes about the book"
            }),
        }