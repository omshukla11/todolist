from django import contrib
from django.utils.html import format_html
from todo.models import Todo
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


# Register your models here.

from .models import Todo, User

class UserAdmin(UserAdmin):
    save_on_top = True
    readonly_fields = ('photo_display', )
    model = User
    list_display = ['username', 'email', 'full_name', 'photo_display']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('profile_pic', 'photo_display')}),
    )

    def photo_display(self, obj):
        return format_html(f'<img src="/media/{obj.profile_pic}" style="height:100px; width:100px">')

admin.site.register(User, UserAdmin)

class TodoAdmin(admin.ModelAdmin):
    # fields = ('task', 'description', 'bydate', 'bytime')
    exclude = ('user', 'completed')
    list_display = ('task','ShortDescription', 'bydate', 'bytime')


admin.site.register(Todo, TodoAdmin)