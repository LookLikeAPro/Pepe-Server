from django.db import models
from .modelMethods import _to_dict

class Picture(models.Model):
	asset = models.CharField(max_length=200)
	uuid = models.CharField(max_length=200)
	to_dict = _to_dict