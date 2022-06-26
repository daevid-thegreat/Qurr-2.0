from django.shortcuts import redirect, render
from pytube import YouTube
import os
# Create your views here.


def downloader(request):
    return render(request, 'ytdownloader.html')

def download(request):
    link = request.GET.get('url')
    yt = YouTube(link)
    title = yt.title 
    video = []
    video = yt.streams.filter(progressive=True).all()
    embed = link.replace("watch?v=", "embed/")
    context = {'title':title, 'video':video, 'embed':embed}
    return render(request,'download.html', context)
    
def download_done(request, resolution):
    global link
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    video = YouTube(link)
    if request.method == "POST":
        video.streams.get_by_resolution(resolution).download(dirs)
        return render(request, 'downloaddone.html')
    else:
        return render(request, 'index.html')   
