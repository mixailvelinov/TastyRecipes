# Generated by Django 5.1.2 on 2024-10-25 18:25

import django.core.validators
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Nickname must be at least 2 chars long!')])),
                ('first_name', models.CharField(max_length=30, validators=[profiles.validators.first_letter_checker])),
                ('last_name', models.CharField(max_length=30, validators=[profiles.validators.first_letter_checker])),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]