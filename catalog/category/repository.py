from rest_framework import serializers
from django.db.models import QuerySet
import django_filters

from catalog.models import Categories
from catalog.category.entity import Category
from functools import cache
from typing import List
from dataclasses import asdict


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('name', 'slug', 'file')


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Categories
        fields = ('name', 'slug')


class CategoryRepository:
    def transform(self, model: Categories) -> Category:
        return Category(
                name=model.name,
                slug=model.slug,
                children=self.get_children(model),
                file=model.file.path if model.file else None
            )

    @staticmethod
    def get_by_slug(slug: str) -> Categories:
        try:
            return Categories.objects.get(slug=slug)
        except Categories.DoesNotExist:
            return None

    @staticmethod
    def get_queryset() -> QuerySet[Categories]:
        return Categories.objects.all()

    @staticmethod
    def serialize(categories: Category) -> list[dict]:
        if type(categories) == list:
            return [asdict(cat) for cat in categories]
        else:
            return asdict(categories)

    @cache
    def tree(self) -> list[Category]:
        base_categories = Categories.objects.filter(parent__isnull=True)
        return [
            self.transform(cat)
            for cat in base_categories
        ]

    @cache
    def get_children(self, category: Categories) -> List[Category]:
        children = Categories.objects.filter(parent=category)

        return [
            self.transform(child)
            for child in children
        ]
