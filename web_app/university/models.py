from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime

class Faculty(models.Model):
    """Факультет"""

    class Meta:
        db_table = "faculties"
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    title = models.TextField(verbose_name='Название факультета')
   
    def __str__(self):
        return f"{self.title}"
    
class Group(models.Model):
    """Группа"""

    class Meta:
        db_table = "groups"
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    number_of_group = models.TextField(verbose_name="Номер группы")
    schedule_of_classes = models.TextField(verbose_name='Расписание занятий')
    faculty = models.ForeignKey(Faculty, on_delete=models.RESTRICT, verbose_name="Факультет")

    def __str__(self):
        return f"{self.number_of_group} {self.schedule_of_classes} {self.faculty}"

class Student(models.Model):
    """Студенты"""

    class Meta:
        db_table = "students"
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    name = models.TextField(verbose_name="Имя студента")
    student_ID = models.TextField(verbose_name="Номер студенческого билета")
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, verbose_name="Группа")

    def __str__(self):
        return f"{self.student_ID} {self.name} {self.group}"
    