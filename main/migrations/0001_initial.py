# Generated by Django 3.1 on 2021-04-05 08:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('language', models.CharField(choices=[('RU', 'RU'), ('KG', 'KG')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_ad', models.ImageField(blank=True, null=True, upload_to='adv_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('language', models.CharField(choices=[('RU', 'RU'), ('KG', 'KG')], max_length=2)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('category', models.ManyToManyField(related_name='post_category', to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_on_main_page/')),
            ],
        ),
        migrations.CreateModel(
            name='PostVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='post_videos/')),
                ('post_video', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_video', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tag', models.CharField(max_length=50)),
                ('tag', models.ManyToManyField(default='', related_name='tags', to='main.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, max_length=255, upload_to='')),
                ('post_image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='image_post', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('is_true', models.BooleanField(default=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main.post')),
            ],
        ),
    ]
