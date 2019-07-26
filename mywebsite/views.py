from django.views.generic import TemplateView

from article.views import ArticlePerCateory


class MyWebsiteHome(TemplateView,ArticlePerCateory):
    template_name = 'index.html'

    def get_context_data(self):
        querysets = self.get_latest_article_each_category()

        context = {
            'last_article_list' : querysets
        }
        return context