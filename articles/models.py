from django.db import models

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title}"

