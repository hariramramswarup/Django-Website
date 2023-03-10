from django.contrib import admin
from django.urls import path, include
from core.sitemap import ArticleSitemap
from core import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', views.index, name='core'),
    path('book/<str:slug>', views.book, name='book'),
    path('search/', views.search, name='search'),
    path('books/', views.books, name='books'),
    path('about', views.about, name='about'),
    path('donate', views.donate, name='donate'),
    path('dmca', views.dmca, name='dmca'),
    path('contact', views.contact, name='contact'),
    path('download/', views.download, name='download'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy/', views.privacy, name='privacy'),
    path('sitemap.xml', sitemap, {'sitemaps': {'article' : ArticleSitemap}},name='django.contrib.sitemaps.views.sitemap')
]