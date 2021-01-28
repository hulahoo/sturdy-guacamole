from django.contrib import admin
from django.contrib.gis import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from main.models import Category, Post, Comment, PostVideo, Video, PostTag, PostImage, ImageAd


class NewAdminForm(forms.ModelForm):
    title_post = forms.CharField(widget=CKEditorUploadingWidget())
    decription = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class ImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class VideoInline(admin.TabularInline):
    model = PostVideo
    extra = 1


class PostAdmin(admin.ModelAdmin):
    form = NewAdminForm
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
admin.site.register(ImageAd)