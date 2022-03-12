from django.contrib import admin

from .models import Post, Port

class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'titulo')
    

class UserAdmin2(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')

admin.site.register(Post, UserAdmin)
admin.site.register(Port, UserAdmin2)