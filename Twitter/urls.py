from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.homepage, name='home'),
   path("search", views.tweet_search, name="search"),
]