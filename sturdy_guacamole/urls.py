from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import PostViewSet, CategoryViewSet, CommentViewSet, PostVideoViewSet, VideoViewSet, PostTagViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('post_video', PostVideoViewSet)
router.register('main_video', VideoViewSet)
router.register('post_tag', PostTagViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
