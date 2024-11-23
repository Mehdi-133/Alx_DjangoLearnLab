from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book,BookAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the CustomUser model.
    """
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (  # Add custom fields to the existing fieldsets
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (  # Add custom fields to the add user form
        ('Additional Info', {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']  # Customize the admin list view
    search_fields = ['username', 'email']  # Add search capabilities for username and email

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
