# Generated by Django 4.1.7 on 2023-03-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_delete_donor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(default='', max_length=30)),
                ('middlename', models.TextField(default='', max_length=30)),
                ('lastname', models.TextField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('area_or', models.TextField(default='Area')),
                ('town', models.TextField(default='')),
                ('id_number', models.CharField(default='GHA-###########-1', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='area_or',
        ),
    ]
