from __future__ import unicode_literals

from django.db import models

# Create your models here.

class city_info(models.Model):
	"""Data base for the third exercise"""
	class Meta(object):
		db_table = 'city_info'

	city_info_country = models.CharField(max_length=25)
	city_info_region = models.CharField(max_length=25)
	city_info_city = models.CharField(max_length=25)

class Orders(models.Model):
	class Meta(object):
		db_table = 'Orders'

	orders_id = models.IntegerField()
	orders_product = models.CharField(max_length=25)
	orders_customer = models.CharField(max_length=25)
	orders_quantity = models.CharField(max_length=25)