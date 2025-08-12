from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Application(models.Model):
    CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer Received'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=CHOICES, default='applied')
    job_link = models.URLField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    resume_version = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} - {self.company_name}"
