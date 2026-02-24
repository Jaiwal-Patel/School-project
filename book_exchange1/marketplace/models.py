from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Grade(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name


class Book(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('GOOD', 'Good'),
        ('FAIR', 'Fair'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        help_text="Include country code, e.g. 971xxxxxxxxx"
    )

    image = models.ImageField(
        upload_to="book_images/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
admin.site.register(Grade)
    
