# Generated by Django 4.1.7 on 2023-04-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_donor_region_donor_user_alter_donor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='user',
        ),
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
