from django.contrib import admin
from main.models import *



class ImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class VideoInline(admin.TabularInline):
    model = PostVideo
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, VideoInline
    ]



class ModelAdmin(admin.ModelAdmin):
    model = Comment
    list_filter = ('is_true', 'post_id')


# class ImageInlineKG(admin.TabularInline):
#     model = PostImageKG
#     extra = 1


# class VideoInlineKG(admin.TabularInline):
#     model = PostVideoKG
#     extra = 1


# class PostAdminKG(admin.ModelAdmin):
#     inlines = [
#         ImageInlineKG, VideoInlineKG
#     ]



# class ModelAdminKG(admin.ModelAdmin):
#     model = CommentKG
#     list_filter = ('is_true', 'post_id')


admin.site.site_header = "Hulahoo"  # отвечает за изменение текста главного поля в админской панели
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, ModelAdmin)
admin.site.register(PostVideo)
admin.site.register(Video)
admin.site.register(PostTag)
admin.site.register(PostImage)
admin.site.register(ImageAd)


# admin.site.register(CategoryKG)
# admin.site.register(PostKG, PostAdminKG)
# admin.site.register(CommentKG, ModelAdminKG)
# admin.site.register(PostVideoKG)
# admin.site.register(PostTagKG)
# admin.site.register(PostImageKG)