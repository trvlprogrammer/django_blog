from django.conf.urls import url

from .views import (
    ArticleListView, 
    ArticleDetailView,
    ArticleListCategoryView,
    CreateArticleView,
    ManageArticle,
    DeleteArticle,
    UpdateArticle
)

urlpatterns = [
        url(r'^manage/update/(?P<pk>\d+)$', UpdateArticle.as_view(), name = 'update'),
        url(r'^manage/delete/(?P<pk>\d+)$', DeleteArticle.as_view(), name = 'delete'),    
        url('^manage/$',ManageArticle.as_view(), name='manage'),
        url(r'^create/$',CreateArticleView.as_view(), name = 'create'),
        url(r'^category/(?P<category>[\w]+)/(?P<page>\d+)$',ArticleListCategoryView.as_view(), name = 'category'),
        url(r'^(?P<page>\d+)$',ArticleListView.as_view(), name = 'list'),
        url(r'detail/(?P<slug>[\w-]+)$', ArticleDetailView.as_view(), name = 'detail'),
    ]