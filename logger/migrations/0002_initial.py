# Generated by Django 4.2.1 on 2023-05-05 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
        ("logger", "0001_initial"),
        ("incident", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscriberassignment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="escalation_policy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="incident.escalationpolicy",
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="guests",
            field=models.ManyToManyField(
                related_name="services",
                through="logger.GuestAssignment",
                to="users.guest",
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="subscribers",
            field=models.ManyToManyField(
                related_name="services",
                through="logger.SubscriberAssignment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="guestassignment",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.guest"
            ),
        ),
        migrations.AddField(
            model_name="guestassignment",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="logger.service"
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="request_handler",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="logger.requesthandler",
            ),
        ),
        migrations.AddField(
            model_name="endpoint",
            name="service",
            field=models.ManyToManyField(related_name="endpoints", to="logger.service"),
        ),
        migrations.AddField(
            model_name="cronhandler",
            name="service",
            field=models.ManyToManyField(related_name="crons", to="logger.service"),
        ),
    ]
