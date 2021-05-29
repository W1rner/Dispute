from django.db import models
from django.contrib.auth.models import User
from time import time
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

COMMENT_SIZE = 280
QUESTION_SIZE = 180
USERNAME_SIZE = 20
CATEGORY_SIZE = 30

class Question(models.Model):
    header = models.CharField(max_length=QUESTION_SIZE)
    text = models.CharField(max_length=COMMENT_SIZE)
    category = models.CharField(max_length=CATEGORY_SIZE, default="Другое")
    user = models.CharField(max_length=USERNAME_SIZE)
    time = models.IntegerField(default=time())
    rating = models.IntegerField(default=0)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.user = user
        instance.save()
        form.save_m2m()
        return instance



# name = models.TextField(unique=True)
# about = models.TextField()
# author = models.TextField()
# all_votes_quantity = models.IntegerField()
# variants = models.TextField()
# variants_values = models.TextField()
# participants = models.TextField()


class Commentary(models.Model):
    parent = models.ForeignKey(Question,
            default=4,
            on_delete=models.CASCADE
            )
    user = models.CharField(max_length=USERNAME_SIZE)
    text = models.CharField(null=True, max_length=COMMENT_SIZE)
    time = models.IntegerField(default=int(time()))
    theory = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
