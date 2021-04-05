"""Создаем сериализатор для моделей"""
from rest_framework import serializers
from main.models import Post, Category, Comment, PostImage, PostTag, PostVideo, Video, ImageAd


class ImageAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAd
        fields = ('image_ad', )


class VideoSerializer(serializers.ModelSerializer):
    """Создаем сериалайзер для видео на главной странице"""
    class Meta:
        """Здесь мы определяем его поля"""
        model = Video
        fields = ('video', )

class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер для категорий"""
    class Meta:
        """Добавление модели и полей"""
        model = Category
        fields = ('id', 'url', 'title', 'slug', 'language')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }



class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для постов"""
    class Meta:
        """Добавление модели и полей"""
        model = Post
        fields = ('id', 'url', 'slug', 'title', 'description', 'category', 'language', 'is_main')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для коментов"""
    class Meta:
        """Добавление модели и полей"""
        model = Comment
        fields = ('id', 'full_name', 'comment', 'post_id')


class CommentDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер для деталей комментов"""
    class Meta:
        """Добавление модели и полей"""
        model = Comment
        fields = ('full_name', 'comment', 'is_true', 'post_id')


class PostImageSerializer(serializers.ModelSerializer):
    """Модели для картинок"""
    class Meta:
        """Добавление модели и полей"""
        model = PostImage
        fields = ('post_image', 'is_main', 'image')


class PostTagSerializer(serializers.ModelSerializer):
    """Создание сериалайзера деталей тегов"""
    class Meta:
        """Определение полей"""
        model = PostTag
        fields = ('title_tag', )


class PostVideoSerializer(serializers.ModelSerializer):
    """Создание сериалайзера деталей видео в постах"""
    class Meta:
        """Определение полей"""
        model = PostVideo
        fields = ('video', )


class PostDetailSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)
    """Создание деталей постов"""
    class Meta:
        """Определение полей""" 
        model = Post
        fields = ('id', 'url', 'slug', 'title', 'is_main', 'language', 'created', 'views', 'description', 'category', 'post_video')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


    def to_representation(self, instance):
        """формирует то что будет показываться пользователю он формирует словарь"""
        representation = super().to_representation(instance)  # здесь мы вызываем родительский метод
        representation['category'] = CategorySerializer(instance.category.all(), many=True, context=self.context).data  # здесь мы выводим все категории, many=TRue для большого количества постов
        representation['post_image'] = PostImageSerializer(instance.image_post.all(), many=True, context=self.context).data  # instance это обькет класса который мы прогоняем через serializer в нашем случаем это obj
        representation['post_video'] = PostVideoSerializer(instance.post_video.all(), many=True, context=self.context).data
        representation['post_tag'] = PostTagSerializer(instance.tags.all(), many=True, context=self.context).data
        print(instance.comment.all())
        if instance.comment is not None:
            representation['comments'] = CommentSerializer(instance.comment.filter(is_true = True), many=True, context=self.context).data
        return representation