from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone_number',  'created_at',)
    list_display_links = ('id', 'email', 'first_name', 'last_name', 'phone_number')
    list_filter = ("is_admin", "is_active", 'is_superuser', 'created_at', 'updated_at')
    ordering = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'created_at', 'updated_at']
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    fieldsets = (
        ('User Credentials', {'fields': ('email',  'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'is_superuser', 'is_admin', 'password1', 'password2'),
        }),
    )
    filter_horizontal = ()
    readonly_fields = ('created_at', 'updated_at')

    # def action(self, obj):
    #     if obj.id:
    #         return mark_safe("<a class='button btn' style='color:green; padding:0 1rem; ' href='/admin/accounts/customuser/{}/change/'>Edit</a>".format(obj.id)
    #                          + "    " + "<a class='button btn' style='color:red; padding:0 1rem; ' href='/admin/accounts/customuser/{}/delete/'>Delete</a>".format(obj.id))
    #     else:
    #         social_button = '<a  href="#">---</a>'
    #         return mark_safe(u''.join(social_button))

admin.site.register(CustomUser, UserAdmin)





####### register resume model
@admin.register(Filldetails)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','email','gender','locality','city','pincode','state','contact','preferredJL','image']
