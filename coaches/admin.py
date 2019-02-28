from django.contrib import admin

# Register your models here.

from .models import Coach
from .models import CoachAdmin

admin.site.register(Coach, CoachAdmin)
