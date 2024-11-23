from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

class Article(models.Model):
    # make sure to visit the django documentation at model field types (django model field types)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False,auto_now_add=False, default=timezone.now)

    def __str__(self):
        return f"{self.id} {self.title}"
    
    def save(self, *args, **kwargs):
        """if self.slug is None:
            self.slug = slugify(self.title)"""
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    instance.slug = slug

pre_save.connect(article_pre_save, sender=Article)




def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = "slug deez nuts"
        instance.save()

post_save.connect(article_post_save, sender=Article)