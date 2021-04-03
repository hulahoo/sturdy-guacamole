"""Создание категорий, постов"""
from django.db import models
from django.db.models.signals import pre_save
from sturdy_guacamole.utils import unique_slug_generator # import from main folder
from django_ckeditor_5.fields import CKEditor5Field


LANGUAGE_CHOICES = (
        ('RU', 'RU'),
        ('KG', 'KG')
    )

class Category(models.Model):
    """Создание модели категории имеет только заголовок"""
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)


    def __str__(self):
        return self.title

class Post(models.Model):
    """Создание модели постов с м2м связью с категорией"""
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    # description = models.TextField()
    description = CKEditor5Field('Text', config_name='extends')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category, related_name='post_category')


    def __str__(self):
        return self.title

class PostTag(models.Model):
    """Создание модели тегов для постов"""
    title_tag = models.CharField(max_length=50)
    tag = models.ManyToManyField(Post, related_name='tags', default='')

    def __str__(self):
        return self.title_tag

class PostImage(models.Model):
    """Создание модели картинок имеет связь с постом"""
    is_main = models.BooleanField(default=False)
    image = models.URLField(max_length=255, blank=True)
    post_image = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image_post', default='')

    

class PostVideo(models.Model):
    """Создание модели видео для постов"""
    url = models.URLField(max_length=200)
    post_video = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_video', default='')


    def __str__(self):
        return self.url

class Comment(models.Model):
    """Создание модели коментариев имеет связь с Постом"""
    full_name = models.CharField(max_length=50, blank=True)
    comment = models.TextField(blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.comment

class Video(models.Model):
    """Создание видео для главной страницы"""
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url

class ImageAd(models.Model):
    image_ad = models.URLField(max_length=255, blank=True)





def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        # i added in main folder of proj new file which named utils.py, there writed func slug generator


pre_save.connect(slug_generator, sender=Category)
pre_save.connect(slug_generator, sender=Post)
