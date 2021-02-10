from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import twitter_id
# Create your views here.


def homepage(request):
    return render(request, 'base.html')


def search(request):
    tweet = request.POST.get('tweet_id')
    print(tweet)
    twitter_id.objects.create(search=tweet)
    return render(request, 'base.html')


class tf_processing(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        tweet = twitter_id.objects.all().order_by('-created').first().search
        data = {
            "sales": 3400,
            "company": 5400,
            "tweet": tweet
        }
        return Response(data)
