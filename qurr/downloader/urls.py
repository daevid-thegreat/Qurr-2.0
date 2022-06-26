from django.urls import path
from downloader.views import downloader, download_done

app_name = 'downloader'

urlpatterns = [
    path('yt-downloader/', downloader),
    path('downloaded/<resolution>/', download_done, name='download_done'),
]