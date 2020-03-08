from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from colegio.models import User, Curso, Asign, Profile

class CustomUserAdmin(UserAdmin):
    """User model admin"""
    list_display = ('id','username','email','first_name','last_name','phone_number','user_type')
    list_filter = ('created', 'modified')

@admin.register(Curso)
class CommentAdmin(admin.ModelAdmin):
    list_display=('nombre_curso', 'profesor','descripcion')

@admin.register(Asign)
class Nota(admin.ModelAdmin):
    list_display=('alumno', 'curso', 'nota')

@admin.register(Profile)  
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'biography')

admin.site.register(User, CustomUserAdmin)