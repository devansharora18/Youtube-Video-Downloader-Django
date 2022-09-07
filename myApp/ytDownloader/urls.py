from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.ytd, name="ytd"),
	path('download/', views.download_page, name="download")
]