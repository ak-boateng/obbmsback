# Generated by Django 4.1.7 on 2023-03-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Donor_Status',
        ),
    ]