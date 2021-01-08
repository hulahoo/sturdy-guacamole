"""Создание вьюшек с помощью ViewSet"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from main.models import Post, Category, Comment, PostVideo, Video
from main.serializers import PostDetailSerializer, CategorySerializer, CommentSerializer, PostVideoSerializer, VideoSerializer


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class PostViewSet(ModelViewSet):
    """Создание предтставления"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'title_post']
    search_fields = ['category', 'title_post']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filteset_fields = ['title_category', ]
    search_fields = ['title_category', ]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['full_name', 'post_id']
    search_fields = ['full_name', 'post_id']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class PostVideoViewSet(ModelViewSet):
    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer
    print("Successfully!")
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]