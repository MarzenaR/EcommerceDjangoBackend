from django.contrib import admin
from homepage_api.models import HomePageInfo

admin.site.register(HomePageInfo)
# zmigrowac trzeba HomePageInfo: python manage.py makemigrations i zatwierdzic python manage.py migrate
