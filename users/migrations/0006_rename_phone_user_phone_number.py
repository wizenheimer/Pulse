# Generated by Django 4.2.1 on 2023-05-16 19:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_usergroups_remove_user_groups_user_groups"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="phone",
            new_name="phone_number",
        ),
    ]
