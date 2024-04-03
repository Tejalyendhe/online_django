from django.contrib import admin
from .models import UserType,Product,PrimaryImageAttachment,SecondaryImageAttachment,Product_type
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = "Type"

class CustomizedUserAdmin (UserAdmin):
    inlines = (CustomUserInline,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(Product)
admin.site.register(Product_type)
admin.site.register(PrimaryImageAttachment)
admin.site.register(SecondaryImageAttachment)
