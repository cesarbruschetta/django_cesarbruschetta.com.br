from django.shortcuts import render

# Create your views here.


def blog_home(request):
    context = {
        'title_page': 'Blog'
    }
    return render(request, 'news_feed/blog.html', context)


def post_blog(request, slug):
    context = {
        'title_page': 'Home'
    }
    return render(request, 'news_feed/single.html', context)
