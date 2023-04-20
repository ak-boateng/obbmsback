# Generated by Django 4.1.7 on 2023-03-31 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_donor_status_alter_donor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='region',
            field=models.TextField(choices=[('ahafo', 'Ahafo Region'), ('ashanti', 'Ashanti Region'), ('bono', 'Bono East Region'), ('brong', 'Brong Ahafo Region'), ('central', 'Central Region'), ('eastern', 'Eastern Region'), ('greater', 'Greater Accra Region'), ('north east', 'North East Region'), ('northern', 'Northern Region'), ('oti', 'Oti Region'), ('savannah', 'Savannah Region'), ('upper east', 'Upper East Region'), ('upper west', 'Upper West Region'), ('western', 'Western Region'), ('western north', 'Western North Region'), ('volta', 'Volta Region')], default='ahafo', max_length=35),
        ),
    ]
