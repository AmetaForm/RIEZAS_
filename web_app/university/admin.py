from django.contrib import admin
from .models import Group, Faculty, Student


class GroupAdmin(admin.ModelAdmin):
    list_display = ("number_of_group","schedule_of_classes")
    search_fields = ("number_of_group","schedule_of_classes")

class FacultyAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

class StudentAdmin(admin.ModelAdmin):
    def my_group(self, obj):
        return obj.group.number_of_group
    def my_faculty(self, obj):
        return obj.group.faculty.title
    def my_schedule(self, obj):
        return obj.group.schedule_of_classes
    
    my_group.short_description = "группа"
    my_faculty.short_description = "факультет"
    my_schedule.short_description = "расписание"

    list_display = ("name","student_ID","my_group","my_faculty","my_schedule")
    search_fields = ("name","student_ID","group__number_of_group","group__faculty__title","group__schedule_of_classes")

admin.site.register(Group, GroupAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)