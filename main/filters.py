import django_filters
from django_filters import rest_framework as filters
from django_filters import ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Category, Post




class CategoryFilter(filters.FilterSet):
    title = ModelChoiceFilter(
        queryset=Category.objects.all(),
        to_field_name='title',
    )

    class Meta:
        model = Category
        fields = ['title', 'language']


#for m2m fields
class PostFilter(filters.FilterSet):
    category = ModelMultipleChoiceFilter(
        queryset=Post.objects.all(),
        to_field_name='title',
        field_name='category__title'
    )

    class Meta:
        model = Post
        fields = ['category', 'language']

