from django.db import models

# Create your models here.
class Goods(models.Model):
	G_Code = models.CharField(max_length = 5)
	G_Name = models.CharField(max_length = 20)
	G_Price = models.IntegerField(default = 10000)
	G_Rate = models.IntegerField(default = 50)
	G_Level = models.IntegerField(default = 2)

	def __str__(self):
		return self.G_Name