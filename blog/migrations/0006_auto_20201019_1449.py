# Generated by Django 3.1.2 on 2020-10-19 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201019_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aproved_comment',
            new_name='aprove_comment',
        ),
    ]
