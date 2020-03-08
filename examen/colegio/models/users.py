from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from utils.models import ColModel


class User(ColModel, AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{8,13}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type']
    

    USER_TYPE_CHOICES = [
        ('1', 'Profesor'),
        ('2', 'Alumno')
    ]

    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, null=False, default=2)


    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username