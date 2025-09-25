from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "username", "is_superuser", "is_active",)
    list_filter = ("email", "username",)
    ordering = ("-username",)
    fieldsets = (
        (None, {"fields": ("email", "username", "password",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions",),})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_active", "is_staff", "groups", "user_permissions",)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)