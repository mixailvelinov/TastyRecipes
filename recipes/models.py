from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from profiles.models import Profile


# Create your models here.


class Recipe(models.Model):

    class CuisineChoices(models.TextChoices):
        FRENCH = 'French', 'French',
        CHINESE = 'Chinese', 'Chinese',
        ITALIAN = 'Italian', 'Italian',
        BALKAN = 'Balkan', 'Balkan',
        OTHER = 'Other', 'Other'

    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(10)
        ]
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineChoices
    )

    ingredients = models.TextField(help_text='Ingredients must be separated by a comma and space.')

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        help_text='Provide the cooking time in minutes.',
        validators=[MinValueValidator(1)]
    )

    image = models.URLField(null=True, blank=True)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def clean(self):
        super().clean()

        if Recipe.objects.filter(title=self.title).count() > 1:
            raise ValidationError({'title': 'We already have a recipe with the same title!'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

