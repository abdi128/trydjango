from django.test import TestCase
from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title


class ArticleTestCase(TestCase):
    def setUp(self):
        self.article_number = 5000
        for i in range(0, self.article_number):
            Article.objects.create(title='test', content='test')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_equal(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.article_number)

    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by("id").first()
        slug = obj.slug
        title = obj.title
        slugified_title = slugify(title)
        self.assertEqual( slugified_title, slug)

    def test_hello_world_not_slug(self):
        obj = Article.objects.filter(slug__iexact='hello world')
        for object in obj:
            slug = obj.slug
            title = obj.title
            slugified_title = slugify(title)
            self.assertNotEqual( slugified_title, slug)

    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()

        new_slugs = []

        for i in range(0, 500):
            instance = slugify_instance_title(obj, save=False)
            new_slugs.append(instance.slug)

        unique_slugs = list(set(new_slugs))

        self.assertEqual(len(new_slugs), len(unique_slugs))