from django.db import models

from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250,blank=True)
    image = URLField(blank=True)
    url = URLField(blank=True)
    tag = CharField(max_length=250,blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title