from django.contrib.sitemaps import Sitemap
from .models import Blog
  
class ArticleSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()
        
    def lastmod(self, obj):
        return obj.time