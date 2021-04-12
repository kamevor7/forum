from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.
from blog.models import ClimbingAreas, Blog, Users


class Areas(admin.ModelAdmin):
    list_display = ('title', 'number_of_routes',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ['title']


admin.site.register(ClimbingAreas, Areas)


class Blogs(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date',)
    list_filter = ('author', 'title',)
    search_fields = ('author',)
    ordering = ['author']


admin.site.register(Blog, Blogs)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UsersInline(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = 'users'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UsersInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
