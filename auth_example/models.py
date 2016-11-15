from re import match
from django.contrib.auth.models import User, UserManager
from django.core.validators import ValidationError
from django.db import models


# Create your models here.
# class CustomUser(User):
	# date_of_birth = models.DateField()
	# sex = models.CharField(max_length=20)

	# objects = UserManager()

	# def clean_username(self):
		# cleaned_username = self.cleaned_data["username"]
		# if match(r'\w+', cleaned_username):
			# return cleaned_username
		# else:
			# raise ValidationError

	# def clean_email(self):
		# cleaned_email = self.cleaned_data["email"]
		# if match(r'\w+', cleaned_email):
			# return cleaned_email
		# else:
			# raise ValidationError
