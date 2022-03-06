import django.db.models
from django.db import models


class Breeds(django.db.models.Model):
    adaptability = models.IntegerField()
    affection_level = models.IntegerField()
    alt_names = models.CharField(max_length=255)
    cfa_url = models.CharField(max_length=255)
    child_friendly = models.IntegerField()
    country_code = models.CharField(max_length=255)
    country_codes = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    dog_friendly = models.IntegerField()
    energy_level = models.IntegerField()
    experimental = models.IntegerField()
    grooming = models.IntegerField()
    hairless = models.IntegerField()
    health_issues = models.IntegerField()
    hypoallergenic = models.IntegerField()
    id = models.CharField(primary_key=True, max_length=255)
    image = models.CharField(max_length=255)
    indoor = models.IntegerField()
    intelligence = models.IntegerField()
    lap = models.IntegerField()
    life_span = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    natural = models.IntegerField()
    origin = models.CharField(max_length=255)
    rare = models.IntegerField()
    reference_image_id = models.CharField(max_length=255)
    rex = models.IntegerField()
    shedding_level = models.IntegerField()
    short_legs = models.IntegerField()
    social_needs = models.IntegerField()
    stranger_friendly = models.IntegerField()
    suppressed_tail = models.IntegerField()
    temperament = models.CharField(max_length=255)
    vcahospitals_url = models.CharField(max_length=255)
    vetstreet_url = models.CharField(max_length=255)
    vocalisation = models.IntegerField()
    weight = models.CharField(max_length=255)
    wikipedia_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Categories(django.db.models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
