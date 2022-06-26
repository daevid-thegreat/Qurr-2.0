from django.urls import path
from downloader.views import download, download_done, downloader

app_name = 'downloader'

urlpatterns = [
    path('yt-downloader/', downloader, name='downloader'),
    path('download/<resolution>/', download_done, name='download_done'),
    path('yt-downloader/download/', download, name='download  video'),
]