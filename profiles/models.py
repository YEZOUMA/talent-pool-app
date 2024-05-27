from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    skills = models.TextField()
    industry = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)

    def __str__(self):
        return self.name
