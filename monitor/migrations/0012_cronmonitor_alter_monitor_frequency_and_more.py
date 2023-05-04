# Generated by Django 4.2 on 2023-05-03 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0005_rename_can_add_teammate_teamassignment_is_member_and_more"),
        ("monitor", "0011_monitor_confirmation_period_monitor_hostname_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CronMonitor",
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
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("cron_url", models.URLField()),
                (
                    "protocol",
                    models.CharField(
                        choices=[("HTTP", "HTTP"), ("HTTPS", "HTTPS")],
                        default="HTTPS",
                        max_length=8,
                    ),
                ),
                ("ip", models.GenericIPAddressField(blank=True, null=True)),
                ("region_US1", models.BooleanField(default=True)),
                ("region_US2", models.BooleanField(default=False)),
                ("region_EU1", models.BooleanField(default=False)),
                ("region_Asia1", models.BooleanField(default=False)),
                ("frequency", models.PositiveIntegerField(default=86400)),
                ("confirmation_period", models.PositiveIntegerField(default=5)),
                (
                    "credentials",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cron",
                        to="monitor.credentials",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="monitor",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("30", "30 Seconds"),
                    ("60", "1 Minute"),
                    ("300", "5 Minutes"),
                    ("1800", "30 Minutes"),
                ],
                default=30,
                max_length=25,
            ),
        ),
        migrations.CreateModel(
            name="CronSubscriberAssignment",
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
                ("start_date", models.DateTimeField(auto_now_add=True)),
                (
                    "cron",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="monitor.cronmonitor",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cronmonitor",
            name="subscribers",
            field=models.ManyToManyField(
                related_name="crons",
                through="monitor.CronSubscriberAssignment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="cronmonitor",
            name="tags",
            field=models.ManyToManyField(
                related_name="cron_monitors", to="monitor.tags"
            ),
        ),
        migrations.AddField(
            model_name="cronmonitor",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.team",
            ),
        ),
    ]