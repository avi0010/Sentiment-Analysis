from django.shortcuts import render
import requests
# Create your views here.


def homepage(request):
    return render(request, 'base.html')


def tweet_search(request):
    search = request.POST.get("tweet_id")
    print(search)
    return render(request, 'base.html')
