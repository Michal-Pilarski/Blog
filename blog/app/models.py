from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(default='', db_index=True, blank=True, null=False)
    
    def get_absolute_url(self):
        return reverse("post", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)    
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.date}'