from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'gender', 'age', 'dob', 'about',
                    'looking_for', 'interests', 'city', 'country','profile_picture']
    list_per_page = 10
    search_fields = ['username', 'email']


admin.site.register(User, UserAdmin)
