from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from student_app.models import CustomUser
from.models import Staffs,Courses,Subjects,Students,Attendance


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(Subjects)
admin.site.register(Courses)
admin.site.register(Staffs)
admin.site.register(Attendance)
admin.site.register(Students)

