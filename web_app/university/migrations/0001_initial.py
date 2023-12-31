# Generated by Django 4.2.6 on 2023-12-07 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(verbose_name="Название факультета")),
            ],
            options={
                "verbose_name": "Факультет",
                "verbose_name_plural": "Факультеты",
                "db_table": "faculties",
            },
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_group", models.TextField(verbose_name="Номер группы")),
                (
                    "schedule_of_classes",
                    models.TextField(verbose_name="Расписание занятий"),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="university.faculty",
                        verbose_name="группа",
                    ),
                ),
            ],
            options={
                "verbose_name": "Группа",
                "verbose_name_plural": "Группы",
                "db_table": "groups",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(verbose_name="Имя студента")),
                (
                    "student_ID",
                    models.TextField(verbose_name="Номер студенческого билета"),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="university.group",
                        verbose_name="Группа",
                    ),
                ),
            ],
            options={
                "verbose_name": "Студент",
                "verbose_name_plural": "Студенты",
                "db_table": "students",
            },
        ),
    ]
