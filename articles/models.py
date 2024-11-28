from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ArticleManager(models.Manager):
    def search(self, query):
        lookups = Q(title__icontains=query) #| Q(content__icontains=query) 
        return self.get_queryset().filter(lookups)

class Article(models.Model):
    # make sure to visit the django documentation at model field types (django model field types)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False,auto_now_add=False, default=timezone.now)

    objects = ArticleManager()

    def __str__(self):
        return f"{self.id} {self.title}"
    
    """def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)"""
    
    def get_absolute_url(self):
        #return f"/article/{self.slug}/"
        return reverse('articles', kwargs={ "pk": self.slug  })

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


pre_save.connect(article_pre_save, sender=Article)

post_save.connect(article_post_save, sender=Article)