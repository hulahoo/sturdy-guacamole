# Generated by Django 3.1 on 2021-01-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210128_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_ad', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]