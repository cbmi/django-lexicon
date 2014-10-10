from django.db import models
from lexicon.models import Lexicon

class Month(Lexicon):
    label = models.CharField(max_length=20)
    value = models.CharField(max_length=20)


class Date(models.Model):
    day = models.SmallIntegerField()
    month = models.ForeignKey(Month)
    year = models.SmallIntegerField()
