from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Breeds(ExportModelOperationsMixin("breeds"), models.Model):
    description = models.CharField(max_length=1023, blank=True)
    id = models.CharField(primary_key=True, max_length=255)
    images = ArrayField(models.CharField(max_length=255, blank=True))
    name = models.CharField(max_length=255, blank=True)
    origin = models.CharField(max_length=255, blank=True)
    temperament = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Categories(ExportModelOperationsMixin("categories"), models.Model):
    id = models.IntegerField(primary_key=True)
    images = ArrayField(models.CharField(max_length=255, blank=True))
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
