from django.contrib import admin

# Register your models here.
from .models import trains,person

admin.site.register(trains)
admin.site.register(person)