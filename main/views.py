"""Создание вьюшек с помощью ViewSet"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from main.models import Post, Category, Comment, PostVideo, Video, PostTag, ImageAd
from main.search import CustomSearchFilter, CategorySearchFilter
from main.serializers import PostDetailSerializer, CategorySerializer, CommentSerializer, PostVideoSerializer, \
    VideoSerializer, PostTagSerializer, ImageAdSerializer


class PostViewSet(ModelViewSet):
    """Создание предтставления"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_backends = [DjangoFilterBackend, CustomSearchFilter]
    filterset_fields = ['title_post', 'category', 'tags']
    search_fields = ['title_post', ]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]

    def retrieve(self, request, pk):
        if request.method == 'GET':
            queryset = self.filter_queryset((self.get_queryset()))
            obj = self.get_object()
            obj.views += 1
            obj.save(update_fields=("views",))
        return super().retrieve(request)


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, CategorySearchFilter]
    filteset_fields = ['title_category', ]
    search_fields = ['title_category', ]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['full_name', 'post_id']
    search_fields = ['full_name', 'post_id']
    permission_classes = [AllowAny, ]


class PostVideoViewSet(ModelViewSet):
    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer
    print("Successfully!")
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class PostTagViewSet(ModelViewSet):
    queryset = PostTag.objects.all()
    serializer_class = PostTagSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]


class ImageAdViewSet(ModelViewSet):
    queryset = ImageAd.objects.all()
    serializer_class = ImageAdSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, ]