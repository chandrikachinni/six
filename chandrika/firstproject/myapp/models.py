from django.db import models

# Create your models here.
class index(models.Model):
    i_name = models.CharField(max_length=50)
    i_email = models.EmailField(max_length=50)
    i_password = models.CharField(max_length=10)


   