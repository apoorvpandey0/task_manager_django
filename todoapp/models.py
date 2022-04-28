from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
        
class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(
        validators=[

        ]
    )
    priority = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
            validate_even,
        ]
    )
    completed = models.BooleanField()

    def __str__(self):
        return self.title + "|" + str(self.completed)
    


