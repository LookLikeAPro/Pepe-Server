from django.db import models
from random import randint
from .modelMethods import _to_dict

class PictureManager(models.Manager):
	def random(self):
		count = self.aggregate(count=models.aggregates.Count('id'))['count']
		random_index = randint(0, count - 1)
		return self.all()[random_index]

class Picture(models.Model):
	asset = models.CharField(max_length=200, unique=True, blank=False)
	dhash = models.CharField(max_length=1024, unique=True)
	uuid = models.CharField(max_length=8, unique=True, blank=False)
	to_dict = _to_dict
	objects = PictureManager()
