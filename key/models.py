from django.db import models
from django.contrib.auth.models import User

class AccessKey(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_of_procurement = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.email} - {self.status}"

