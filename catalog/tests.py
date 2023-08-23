from django.test import TestCase
from catalog.models import *
from catalog.repositories.category_repository import CategoryRepository
from catalog.entities.category import Category


class TestCategories(TestCase):
    def setUp(self) -> None:
        self.repo = CategoryRepository()

        self.cat1 = Categories(name='Cat1', slug='cat1')
        self.cat1.save()

        self.cat2 = Categories(name='Cat2', slug='cat2', parent=self.cat1)
        self.cat2.save()

        self.cat3 = Categories(name='Cat3', slug='cat3', parent=self.cat2)
        self.cat3.save()

    def test_tree(self):
        """test tree"""

        tree = self.repo.list()
        parent = self.repo.get_parent(self.cat3)
        children = self.repo.get_children(self.cat2)

        assert len(tree) == 1 and len(tree[0].children) == 1 and len(tree[0].children[0].children) == 1
        assert isinstance(parent, Category) and len(parent.children) == 1
        assert len(children) == 1

        print(self.repo.list())
        print(parent)
        print(children)
