from django.contrib import admin
# from .models import UserProfile
# from django.contrib.auth.models import User

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False

# class UserAdmin(admin.ModelAdmin):
#     inlines = (UserProfileInline,)

# admin.site.register(User)

from django.contrib.auth.admin import UserAdmin as CustomuserAdmin
from .models import CustomUser

class UserAdmin(CustomuserAdmin):
    pass

admin.site.register(CustomUser, UserAdmin)