from django.db import models
import os
import uuid
import datetime
from django.utils.crypto import get_random_string


def get_upload_path(instance, filename):
    return os.path.join("{0}".format(instance.fk_user.username), filename)


def generate_uuid():
    return uuid.uuid4().hex[:10]


def get_RandomString():
    return get_random_string(7, '0123456789qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM')


class Category(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=25, default=get_RandomString, unique=True, blank=True)
    name = models.CharField(max_length=20, null=False, blank=False)

    # icon = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=25, default=get_RandomString, unique=True, blank=True)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=20, default=get_RandomString, unique=True, blank=True)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=40, default=get_RandomString, unique=True, blank=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    img = models.ImageField(upload_to=get_upload_path)
    fk_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    fk_difficult = models.ForeignKey(Difficulty, on_delete=models.CASCADE, null=True)
    fk_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    steps = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name




class Measurement(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    slug = models.SlugField(max_length=10, default=get_RandomString, unique=True, blank=True)
    name = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    fk_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, related_name='recipe_ingredient')
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    fk_measurement_unit = models.ForeignKey(Measurement, on_delete=models.CASCADE, null=True)
    main_ingredient = models.BooleanField()
    amount = models.FloatField()

    def __str__(self):
        return '%s - %d%s' % (self.fk_product.name, self.amount, self.fk_measurement_unit.name)


class UserLike(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True, max_length=10)
    fk_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    fk_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
