# Generated by Django 2.1.4 on 2019-12-05 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_pharmacyimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PharmacyImage',
            new_name='AppImage',
        ),
    ]