from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    
class Classes(models.Model):
    class_number = models.CharField(max_length=100)
    class_name = models.TextField()
    class_description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="classes")

    def __str__(self):
        return self.title