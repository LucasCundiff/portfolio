# Generated by Django 5.0.7 on 2024-08-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='skillSet',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skillSetParent',
        ),
        migrations.AddField(
            model_name='skill',
            name='skillSet',
            field=models.CharField(choices=[('Front End', 'Front End'), ('Back End', 'Back End'), ('Database', 'Database')], default='Front End', max_length=255),
        ),
    ]
