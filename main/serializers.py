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
        fields = ('url', )


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер для категорий"""
    class Meta:
        """Добавление модели и полей"""
        model = Category
        fields = ('id', 'title_category')


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для постов"""
    class Meta:
        """Добавление модели и полей"""
        model = Post
        fields = ('id', 'title_post', 'description', 'category')


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
        fields = ('post', 'is_main', 'image')


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
        fields = ('url', )


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('image', )


class PostDetailSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)
    """Создание деталей постов"""
    class Meta:
        """Определение полей"""
        model = Post
        fields = ('id', 'title_post', 'description', 'category', 'post_video', 'created', 'views', 'tags')

    #
    # def _get_image_url(self, obj):
    #     """Мы получаем url первой картинки"""
    #     request = self.context.get('request')  # это у нас словарь и поэтому нужен метод get
    #     image_obj = obj.image_post.first()  # если картинка есть то возвращает обьект
    #     if image_obj is not None and image_obj.image:  # здесь мы проверяем если есть картинка то он вытаскивает url
    #         url = image_obj.image.url
    #         if request is not None:  # если request нам пришел не None
    #             url = request.build_absolute_uri(url)  # то новое значение url будет абсолютным путем старого url
    #         return url  # и возвращает путь
    #     return "No Image"  # а если картинки нету то возвращает пустую строку


    def to_representation(self, instance):
        """формирует то что будет показываться пользователю он формирует словарь"""
        representation = super().to_representation(instance)  # здесь мы вызываем родительский метод
        representation['category'] = CategorySerializer(instance.category.all(), many=True).data  # здесь мы выводим все категории, many=TRue для большого количества постов
        representation['post_image'] = PostImageSerializer(instance.image_post.all(), many=True).data  # instance это обькет класса который мы прогоняем через serializer в нашем случаем это obj
        representation['post_video'] = PostVideoSerializer(instance.post_video.all(), many=True).data
        representation['post_tag'] = PostTagSerializer(instance.tags.all(), many=True).data
        print(instance.comment.all())
        if instance.comment is not None:
            representation['comments'] = CommentSerializer(instance.comment.filter(is_true = True), many=True).data
        return representation