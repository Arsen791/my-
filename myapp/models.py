from django.db import models
class zat(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()