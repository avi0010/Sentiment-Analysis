from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.homepage, name='home'),
   path("api", views.tf_processing.as_view()),
]