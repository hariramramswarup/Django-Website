from unittest import loader
from django.shortcuts import render
from django.core.paginator import Paginator
from core.models import Blog
from django.db.models import Q

def index (request):
    blogs = Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'index.html', context)

def books (request):
    blogs = Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'books.html', context)

def book (request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {'blog': blog}
        return render(request, 'book.html', context)
    except Blog.DoesNotExist:
        context = {'message': 'Blog post not found'}
        return render(request, '404.html', context, status=404)

def search(request):
    query = request.GET.get('q')
    query_list = query.split()
    results = Blog.objects.none()
    for word in query_list:
        results = results | Blog.objects.filter(Q(title__contains=word) | Q(content__contains=word)).order_by('-time')
    paginator = Paginator(results, 5)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    if len(results) == 0:
        message = "Sorry, no book found. Try another"
    else:
        message = ""
    return render(request, 'search.html', {'results': results, 'query': query, 'message': message})

def category(request, category):
    category_posts = Blog.objects.filter(category=category).order_by('-time')
    if not category_posts:
        message = f"No Book found in category: '{category}'"
        return render(request, "category.html", {"message": message})
    paginator = Paginator(category_posts, 5)
    page = request.GET.get('page')
    category_posts = paginator.get_page(page)
    return render(request, "category.html", {"category": category, 'category_posts': category_posts})


def download (request,):
    context = {}
    system = request.POST.get('system')
    context['system'] = system
    return render(request, 'download.html', context)

def categories(request):
    all_categories = Blog.objects.values('category').distinct().order_by('category')
    return render(request, "categories.html", {'all_categories': all_categories})

def about (request):
    return render(request, 'about.html')

def privacy (request):
    return render(request, 'privacypolicy.html')

def disclaimer (request):
    return render(request, 'disclaimer.html')

def dmca(request):
    return render(request, 'dmca.html')

def contact (request):
    return render(request, 'contact.html')

def donate (request):
    return render(request, 'donate.html')