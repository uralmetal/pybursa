from django.contrib import admin

# Register your models here.

from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']

admin.site.register(Feedback, FeedbackAdmin)