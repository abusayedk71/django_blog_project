# Generated by Django 3.1.2 on 2020-10-18 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='publish_date',
        ),
    ]
