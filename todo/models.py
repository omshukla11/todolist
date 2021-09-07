from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

# Create your models here.

class User(AbstractUser):
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    username    = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='image/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']  #USERNAME_FIELD and password are required by default

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

class Todo(Model):
    task        = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    bydate      = models.DateField()
    bytime      = models.TimeField()
    completed   = models.BooleanField(default=False)
    user        = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

    def ShortDescription(self):
        return format_html(f'<span style="color:green; font-family: Comic Sans MS">{self.description[:50]+"..."}</span>')