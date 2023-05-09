# Generated by Django 4.2.1 on 2023-05-09 13:46

from django.db import migrations, models
import incident.models


class Migration(migrations.Migration):
    dependencies = [
        ("incident", "0007_escalationaction_level"),
    ]

    operations = [
        migrations.RenameField(
            model_name="escalationlevel",
            old_name="delay_for",
            new_name="delay",
        ),
        migrations.RenameField(
            model_name="escalationlevel",
            old_name="repeat_for",
            new_name="repeat",
        ),
        migrations.RemoveField(
            model_name="escalationaction",
            name="system",
        ),
        migrations.AddField(
            model_name="escalationaction",
            name="intent",
            field=models.CharField(
                blank=True,
                choices=[("Alert", "Alert"), ("Resolve", "Resolve")],
                default="Alert",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="escalationlevel",
            name="days",
            field=models.CharField(
                default="1234567",
                help_text="Denotes the days for which incident would be triggered",
                max_length=7,
            ),
        ),
        migrations.AddField(
            model_name="escalationlevel",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="escalationlevel",
            name="start_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="escalationlevel",
            name="timezone",
            field=models.CharField(
                blank=True,
                default="UTC",
                max_length=255,
                null=True,
                validators=[incident.models.validate_timezone],
            ),
        ),
        migrations.AddField(
            model_name="escalationlevel",
            name="urgency",
            field=models.PositiveIntegerField(
                default=1, help_text="Denotes the urgency of the incident"
            ),
        ),
        migrations.AddField(
            model_name="escalationpolicy",
            name="impact",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="escalationpolicy",
            name="repeat",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="escalationpolicy",
            name="urgency",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="escalationaction",
            name="entity_type",
            field=models.CharField(
                choices=[
                    ("Email", "Email"),
                    ("EmailList", "EmailList"),
                    ("Phone", "Phone"),
                    ("PhoneList", "PhoneList"),
                    ("Webhook", "Webhook"),
                    ("WebhookList", "WebhookList"),
                    ("ID", "ID"),
                    ("IDList", "IDList"),
                    ("Group", "Group"),
                    ("GroupList", "GroupList"),
                ],
                default="Attribute",
                max_length=255,
            ),
        ),
    ]
