from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    # level = models.PositiveSmallIntegerField(default=1)
    # score = models.CharField(validators=[validate_comma_separated_integer_list], default=[0], max_length=1000)


