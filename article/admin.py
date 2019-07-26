from django.contrib import admin

# Register your models here.

from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    	readonly_fields=[
		'slug',
		'updated',
		'published',
	]

class CategoryAdmin(admin.ModelAdmin):
    	readonly_fields=[
		'slug',
        'updated',
		'published',
	]

admin.site.register(Article, ArticleAdmin),
admin.site.register(Category, CategoryAdmin)