# Generated by Django 3.1 on 2021-01-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
