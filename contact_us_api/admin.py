from django.contrib import admin
from contact_us_api.models import CompanyInfo

admin.site.register(CompanyInfo)
# zmigrowac trzeba HomePageInfo: python manage.py makemigrations i zatwierdzic python manage.py migrate

