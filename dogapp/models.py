from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
def between_one_and_five(value):
    if value < 1 or value > 5:
        raise ValidationError('Value must be between 1 and 5')

class Breed(models.Model):
    class SizeOptions(models.TextChoices):
        TINY = "Tiny", _("Tiny")
        SMALL = "Small", _("Small")
        MEDIUM = "Medium", _("Medium")
        LARGE = "Large", _("Large")

    name = models.CharField(max_length=50)
    size = models.CharField(max_length=6, choices=SizeOptions.choices)
    friendliness = models.IntegerField(validators=[between_one_and_five])
    trainability = models.IntegerField(validators=[between_one_and_five])
    sheddingAmount = models.IntegerField(validators=[between_one_and_five])
    exerciseNeeds = models.IntegerField(validators=[between_one_and_five])

class Dog(models.Model):
    class GenderOptions(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False, blank=False)
    gender = models.CharField(max_length=1, choices = GenderOptions)
    color = models.CharField(max_length=20)
    favoriteFood = models.CharField(max_length=30)
    favoriteToy = models.CharField(max_length=30)