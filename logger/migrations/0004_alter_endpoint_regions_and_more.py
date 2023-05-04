# Generated by Django 4.2 on 2023-05-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logger", "0003_alter_endpoint_regions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="endpoint",
            name="regions",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="requesthandler",
            name="auth_password",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="requesthandler",
            name="auth_username",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="requesthandler",
            name="body",
            field=models.JSONField(default=list),
        ),
    ]
