from django.contrib import admin
from django.contrib.auth.models import User


class UserAdmin(admin.ModelAdmin):  # change admin styles
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'email',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    sortable_by = ['username', 'first_name', 'last_name', 'is_staff']
    readonly_fields = ['last_login', 'date_joined']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
