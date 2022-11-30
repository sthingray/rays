from django.shortcuts import render
import json

# Create your views here.
def home(request):
    return render(request, 'team_app/home.index', {})

