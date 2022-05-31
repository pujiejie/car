from django.db import models

# Create your models here.

class Yezhu(models.Model):
	full_name = models.CharField(max_length=20)
	h_number = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

class License(models.Model):
	p_number = models.CharField(max_length=20)
	yezhu = models.ForeignKey(Yezhu, on_delete=models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

