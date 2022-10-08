# Generated by Django 3.2.13 on 2022-10-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnonymousLogs",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("path", models.CharField(max_length=128)),
                ("user_agent", models.CharField(blank=True, max_length=128)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Anonymous Logs",
                "verbose_name_plural": "Anonymous Logs",
                "ordering": ["-timestamp"],
            },
        ),
    ]
