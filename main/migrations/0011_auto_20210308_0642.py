# Generated by Django 3.1 on 2021-03-08 06:42

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(default=1, verbose_name='Text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
