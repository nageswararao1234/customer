# Generated by Django 2.2 on 2019-12-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Mobile', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('City', models.CharField(max_length=50)),
            ],
        ),
    ]
