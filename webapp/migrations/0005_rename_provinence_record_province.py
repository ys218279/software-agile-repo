# Generated by Django 4.2.5 on 2023-09-21 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_rename_province_record_provinence_alter_record_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='provinence',
            new_name='province',
        ),
    ]