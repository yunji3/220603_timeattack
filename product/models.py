from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'category'

    category = models.CharField(max_length=256)

class Drink(models.Model):
    class Meta:
        db_table = 'drink'

    drink_name = models.CharField(max_length=20)
    drink_category = models.ForeignKey(Category, on_delete=models.CASCADE)

