from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^tweet_search/$', views.tweet_search, name="tweet_search"),
]
  