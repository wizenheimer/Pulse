# Generated by Django 4.2.1 on 2023-05-05 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("incident", "0003_oncallcalendar"),
        ("logger", "0004_service_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="calendar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="incident.oncallcalendar",
            ),
        ),
    ]
