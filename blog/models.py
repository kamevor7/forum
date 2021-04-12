from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/')


class ClimbingAreas(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    number_of_routes = models.IntegerField()
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title + ' | ' + str(self.number_of_routes)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now())
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title + ' | ' + str(self.title)

    def summary(self):
        return self.content[:50]

    def pub_date(self):
        return self.publication_date.strftime('%b %e %Y')
