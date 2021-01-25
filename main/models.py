"""Создание категорий, постов"""
from django.db import models


class Category(models.Model):
    """Создание модели категории имеет только заголовок"""
    title_category = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.title_category


class Post(models.Model):
    """Создание модели постов с м2м связью с категорией"""
    title_post = models.CharField(max_length=100)
    description = models.TextField()
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category, related_name='post_category')


    def __str__(self):
        return self.title_post


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
    email = models.EmailField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.comment


class Video(models.Model):
    """Создание видео для главной страницы"""
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url