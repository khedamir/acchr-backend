from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry
from app import settings
from .models import User, Image


class CustomUserAdmin(UserAdmin):
    fieldsets = ((None, {'fields': ('username', 'password', 'full_name')}),
                 (None, {'fields': ('is_active',)}))
    add_fieldsets = [(None, {'fields': ('username', 'full_name', 'password1', 'password2')})]
    model = User
    list_display = ['username', 'full_name', 'date_joined', 'is_active']
    search_fields = ['full_name']
    list_filter = ['is_active']


class CustomLogEntry(ModelAdmin):
    model = LogEntry
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]
    list_display = [
        'user',
        'action_flag',
        'content_type',
        'action_time',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CustomImageAdmin(ModelAdmin):
    def image_tag(self, image):
        return format_html('<img width="300px" height="300px" src="{}{}"/>'.format(settings.MEDIA_URL, image.url))

    image_tag.short_description = 'Превью'
    readonly_fields = ['image_tag']


admin.site.unregister(Group)
admin.site.register(LogEntry, CustomLogEntry)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Image, CustomImageAdmin)
