from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    text = models.CharField(max_length = 200)

    def __str__(self):
        return self.text 

class Comments(models.Model): 
    item = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    text = models.TextField(max_length = 100)

    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text

class Pizza_Pic(models.Model):
    pic = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    pic_file = models.ImageField(null = True)