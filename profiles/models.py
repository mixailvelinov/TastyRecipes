from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import first_letter_checker


# Create your models here.


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(2, message='Nickname must be at least 2 chars long!')]
    )

    first_name = models.CharField(
        max_length=30,
        validators=[first_letter_checker]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[first_letter_checker]
    )

    chef = models.BooleanField(default=False)

    bio = models.TextField(blank=True, null=True)

