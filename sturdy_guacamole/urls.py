from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import PostViewSet, CategoryViewSet, CommentViewSet, PostVideoViewSet, VideoViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('post_video', PostVideoViewSet)
router.register('main_video', VideoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]