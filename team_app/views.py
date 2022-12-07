from django.shortcuts import render
from django.http import Http404
import json

# Create your views here.
def home(request):
    return render(request, 'team_app/home.index', {})

def index(request):
    if request.method == "POST":
        article = News(
            title=request.POST['title'], body=request.POST['text'], grade=request.POST["grade"])
        article.save()

    try:
        news = News.objects.order_by('-posted_at')
    except News.DoesNotExist:
        raise Http404('this objects does not exist.')

    context = {
        'news': news,
    }

    return render(request, 'team_app/home.html', context)


def mypage(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExit:
        raise Http404("blog does not exit")

    context = {
        "news": news
    }

    return render(request, 'team_app/mypage.html', context)
