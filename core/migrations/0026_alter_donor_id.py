# Generated by Django 4.1.7 on 2023-04-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_donor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
