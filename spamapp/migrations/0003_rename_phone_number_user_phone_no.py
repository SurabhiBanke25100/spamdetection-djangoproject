# Generated by Django 4.2.2 on 2023-07-03 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spamapp', '0002_user_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone_no',
        ),
    ]