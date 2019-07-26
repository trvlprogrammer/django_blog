from django.shortcuts import render

# Create your views here.

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	DeleteView, 
	UpdateView
)
from django.urls import reverse_lazy

# load model
from .models import Article, Category

from .forms import ArticleForm

class UpdateArticle(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article/article_update.html'

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'article/article_delete_confirmation.html'
    success_url = reverse_lazy('article:manage')

class ManageArticle(ListView):
    model = Article
    template_name = 'article/article_manage.html'
    context_object_name = 'articles'

class CreateArticleView(CreateView):
    form_class = ArticleForm
    template_name = 'article/article_create.html'


class ArticleListCategoryView(ListView):
    model   = Article
    template_name = "article/article_category_list.html"
    context_object_name = "articl_list_category"
    ordering = ["-published"]
    model_category = Category
    paginate_by = 2
    def get_queryset(self):
        category_id = self.model_category.objects.filter(name=self.kwargs['category'])
        self.queryset = self.model.objects.filter(category = category_id[0].id)
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        
        categorys = self.model_category.objects.all().exclude(name=self.kwargs['category'])
        print(categorys)
        self.kwargs.update({'categorys' : categorys})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)	



class ArticleListView(ListView):
    model = Article
    model_category = Category
    template_name = 'article/article_list.html'
    context_object_name = 'article_list'
    ordering = ['-published']
    paginate_by = 2
 
    def get_context_data(self, *args, **kwargs):
        
        categorys = self.model_category.objects.all()
        print(categorys)
        self.kwargs.update({'categorys' : categorys})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)	
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'
    model_category = Category

    def get_context_data(self, *args, **kwargs):
        
        categorys = self.model_category.objects.all()
        print(self.object.category.id)
        
        self.kwargs.update({'categorys' : categorys})
        same_article = self.model.objects.filter(category=self.object.category.id).exclude(id=self.object.id)
        print(same_article)
        self.kwargs.update({'same_article' : same_article})
        kwargs = self.kwargs
        print (kwargs)
        return super().get_context_data(*args,**kwargs)	

class ArticlePerCateory():
    model_article = Article
    model_category = Category

    def get_latest_article_each_category(self):
        category_list = self.model_category.objects.all()
        queryset = []


        for category in category_list :

            article = self.model_article.objects.filter(category=category).latest('published')
            queryset.append(article)
        
        return queryset