from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Вы не ввели Логин")
        if not email:
            raise ValueError("Вы не ввели Email")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password):
        return self._create_user(username, email, password)

    def create_superuser(self, username, email, password):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    # age = models.PositiveSmallIntegerField()
    # mental_age = models.PositiveSmallIntegerField()
    # is_prime = models.BooleanField()
    # prime_duration = models.DurationField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.username
