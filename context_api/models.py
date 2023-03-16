from django.db import models

class NavbarOptions(models.Model):
    '''
    Example of:
    Homepage
    /home/
    '''
    name = models.CharField(max_length=100)
    anchor = models.CharField(max_length=50)