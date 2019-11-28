from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Voucher(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()
    valid_to = modesl.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),
                                    MaxValueValidator(10)]