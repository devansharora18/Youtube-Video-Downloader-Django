from unicodedata import name
from django.urls import path, include
from . import views

app_name = 'YT-downloader'

urlpatterns = [
	path('', views.ytd, name="ytd"),
	path('download/', views.download_page, name="download"),
	path('download/<res>/', views.success, name="success")
]