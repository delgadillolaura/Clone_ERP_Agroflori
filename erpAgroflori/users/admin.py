from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Person, WorkRecord
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Person)
admin.site.register(WorkRecord)