# Generated by Django 2.2 on 2019-12-22 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coustomers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coustomer',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='coustomer',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='coustomer',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='coustomer',
            old_name='Name',
            new_name='name',
        ),
    ]
