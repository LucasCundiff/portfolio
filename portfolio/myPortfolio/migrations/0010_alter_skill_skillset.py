# Generated by Django 5.0.7 on 2024-08-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0009_project_projectfeatured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skillSet',
            field=models.CharField(choices=[('Front End', 'Front End'), ('Back End', 'Back End'), ('Database', 'Database'), ('ToolTech', 'ToolTech')], default='Front End', max_length=255),
        ),
    ]
