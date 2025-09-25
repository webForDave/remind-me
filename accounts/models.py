from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super user must have is_staff set to true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super user must have is_superuser set to true")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Super user must have is_active set to true")
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=10, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username