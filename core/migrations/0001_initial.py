# Generated by Django 4.1.6 on 2023-02-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TaskModel",
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
                ("name", models.CharField(max_length=250, verbose_name="Имя")),
                (
                    "description",
                    models.CharField(max_length=2000, verbose_name="Описание"),
                ),
                ("deadline", models.DateTimeField(verbose_name="Контрольный срок")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "В ожидании"),
                            ("in_progress", "В работе"),
                            ("cancelled", "Отменено"),
                            ("done", "Выполнено"),
                        ],
                        default="pending",
                        max_length=32,
                        verbose_name="Статус",
                    ),
                ),
            ],
        ),
    ]
