from django.shortcuts import redirect, render
from pytube import YouTube
import os
# Create your views here.


def downloader(request):
    return render(request, 'ytdownloader.html')

def download(request):
    global url
    url = request.POST['youtube-url']
    yt = YouTube(url)
    title = yt.title 
    video = []
    video = yt.streams.filter(progressive=True).all()
    embed = url.replace("watch?v=", "embed/")
    context = {'title':title, 'video':video, 'embed':embed}
    return render(request,'download.html', context)
    
def download_done(request, resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == "POST":
        yt = YouTube(url).streams.get_by_resolution(resolution)
        yt.download(dirs)
        return render(request, 'downloaddone.html')
    else:
        return render(request, 'index.html')   
