from django.db import models

# Create your models here.
class userdetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=10)

PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

