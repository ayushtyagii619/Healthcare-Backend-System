from django.contrib import admin
from .models import User,Patient, Doctor
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class NewUserAdmin(UserAdmin):
    list_display = ('id','email','name','is_active')
    list_filter = ('id','is_active')
    fieldsets = (
        ('User Credentials',{'fields':('email','password')}),
        ('Personal info',{'fields':('name',)}),
        ('Permissions',{'fields':('is_superuser',)}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','name','password1','password2'),
        }),

    )
    search_fields  = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(User,NewUserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor)
