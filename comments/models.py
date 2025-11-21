from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    SENTIMENT_CHOICES = [
        ('positive','Positive'),
        ('negative','Negative'),
        ('neutral','Neutral'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    sentiment = models.CharField(max_length=10, choices = SENTIMENT_CHOICES)
    confidence = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentiment}"

