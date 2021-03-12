# Generated by Django 3.1 on 2021-03-08 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210308_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryKG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostKG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField()),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('category', models.ManyToManyField(related_name='post_category_kg', to='main.CategoryKG')),
            ],
        ),
        migrations.CreateModel(
            name='PostVideoKG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('post_video', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_video_kg', to='main.postkg')),
            ],
        ),
        migrations.CreateModel(
            name='PostTagKG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tag', models.CharField(max_length=50)),
                ('tag', models.ManyToManyField(default='', related_name='tags_kg', to='main.PostKG')),
            ],
        ),
        migrations.CreateModel(
            name='PostImageKG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('image', models.URLField(blank=True, max_length=255)),
                ('post_image', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='image_post_kg', to='main.postkg')),
            ],
        ),
        migrations.CreateModel(
            name='CommentKG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('is_true', models.BooleanField(default=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_kg', to='main.postkg')),
            ],
        ),
    ]
