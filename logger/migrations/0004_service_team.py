# Generated by Django 4.2.1 on 2023-05-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
        ("logger", "0003_remove_endpoint_is_active_remove_endpoint_is_public_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="services",
                to="users.team",
            ),
        ),
    ]