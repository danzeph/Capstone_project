# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser

# from inventory import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field is required")

#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('role', 'admin')

#         return self.create_user(email, first_name, last_name, password, **extra_fields)
    

# class User(AbstractUser):
  
#     username = None
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def __str__(self):
#         return f"{self.email} as {self.role}"
# Commented it out cause of time