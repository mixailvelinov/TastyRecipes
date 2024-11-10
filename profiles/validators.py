from django.core.exceptions import ValidationError


def first_letter_checker(value):
    if not value[0].isupper():
        raise ValidationError('Name must start with a capital letter!')

    return value

