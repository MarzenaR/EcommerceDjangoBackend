
from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone_no = models.CharField(max_length=60)

    #  django-admin startapp users tworze nowy katalog na nowa apke USERS
    
