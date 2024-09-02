from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_managment_app.models import CustomerUser

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomerUser,UserModel)