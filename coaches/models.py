from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import BooleanFieldListFilter
# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=70)
    skype = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.user.username

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'coach_first_name', 'coach_last_name', 'gender', 'skype', 'description']
    def coach_first_name(self, obj):
        return obj.user.first_name
    coach_first_name.admin_order_field = 'coach__first_name'
    def coach_last_name(self, obj):
        return obj.user.last_name
    coach_last_name.admin_order_field = 'coach__last_name'
    list_filter = ['gender', 'user__is_staff']
