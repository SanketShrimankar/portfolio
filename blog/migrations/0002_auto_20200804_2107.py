# Generated by Django 2.0.2 on 2020-08-04 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='pub_time',
        ),
    ]
