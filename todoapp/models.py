from django.db import models
from accounts.models import User
import datetime

# Create your models here.
class TodoItem(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content