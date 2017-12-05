from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^place/search/$', views.place_text_search, name="place-search"),
	url(r'^place/detail/$', views.place_detail, name="place-detail"),
]