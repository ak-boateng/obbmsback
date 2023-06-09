# Generated by Django 4.1.7 on 2023-03-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_delete_donor'),
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
                ('phone_number', models.CharField(default='##########', max_length=10)),
                ('area_or', models.TextField(default='Area')),
                ('town', models.TextField(default='')),
                ('id_number', models.CharField(default='GHA-###########-1', max_length=30)),
                ('donor_number', models.IntegerField(default=0)),
                ('donor_card', models.CharField(default='NBS/20/##########/', max_length=30)),
                ('name_of_patient', models.TextField(default='', max_length=200)),
                ('hospital', models.CharField(default='', max_length=200)),
                ('ward', models.CharField(default='Ward #', max_length=10)),
            ],
        ),
    ]
