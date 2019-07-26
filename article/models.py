from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField()
    published   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True) 
    slug        = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.name)
        super().save()
    
    def get_absolute_url(self):
        url_slug = {'slug' : self.slug}
        return reverse('category:detail', kwargs = url_slug)
    
    def __str__(self):
        return "{}. {}".format(self.id, self.name)


class Article(models.Model):
    title       = models.CharField(max_length=255)
    body        = models.TextField()
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    published   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
    def get_absolute_url(self):
        url_slug = {'slug' : self.slug}
        return reverse('article:detail', kwargs = url_slug)


    def __str__(self):
        return "{}. {}".format(self.id, self.title)

