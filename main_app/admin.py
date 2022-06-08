from django.contrib import admin
from .models import Client, Interview, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Client)
admin.site.register(Interview)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class CustomizedUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
