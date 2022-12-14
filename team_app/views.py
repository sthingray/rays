from django.shortcuts import render
from django.http import Http404
import json

# Create your views here.
def home(request):
    return render(request, 'team_app/home.html')

def mypage(request):
    return render(request, 'team_app/mypage.html')

def lecture1(request):
    return render(request, 'team_app/授業ページ.html')

def lecture2(request):
    return render(request, 'team_app/授業ページ2.html')

def func(request):
    return render(request, 'team_app/関数.html')

def calcu(request):
    return render(request, 'team_app/四則演算.html')

def assi(request):
    return render(request, 'team_app/代入と式の値.html')

def functest(request):
    return render(request, 'team_app/関数問題.html')

def calcutest(request):
    return render(request, 'team_app/四則演算問題.html')

def alltest(request):
    return render(request, 'team_app/演習問題.html')


