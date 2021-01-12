from django.contrib import admin

from main.models import Category, Post, Comment, PostVideo, Video, PostTag, PostImage


class ImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class VideoInline(admin.TabularInline):
    model = PostVideo
    extra = 1


# class TagInline(admin.TabularInline):
#     model = PostTag


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, VideoInline
    ]


class ModelAdmin(admin.ModelAdmin):
    model = Comment
    list_filter = ('is_true', 'post_id')


admin.site.site_header = "Hulahoo"  # отвечает за изменение текста главного поля в админской панели
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, ModelAdmin)
admin.site.register(PostVideo)
admin.site.register(Video)
admin.site.register(PostTag)
admin.site.register(PostImage)