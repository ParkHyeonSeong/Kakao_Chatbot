from django.contrib import admin
from .models import USER
from .models import RECIPE

# Register your models here.
admin.site.register(USER)
admin.site.register(RECIPE)