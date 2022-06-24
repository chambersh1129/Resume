# Generated by Django 3.2.13 on 2022-06-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hobby",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=64)),
                ("description", models.TextField()),
                ("img", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tag", models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Milestone",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=64)),
                ("description", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("job", "Job"),
                            ("role", "Role"),
                            ("cert", "Certification"),
                            ("edu", "Education"),
                            ("proj", "Project"),
                        ],
                        max_length=4,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("tags", models.ManyToManyField(blank=True, to="resume.Tag")),
            ],
            options={
                "ordering": ["start_date"],
            },
        ),
    ]
