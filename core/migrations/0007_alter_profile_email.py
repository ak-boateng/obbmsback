# Generated by Django 4.1.7 on 2023-03-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_area_or'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='user@email.com', max_length=254),
        ),
    ]
