from django.shortcuts import redirect, render
from pytube import YouTube
import os
from django_globals import globals
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
    if request.method == 'POST':
        homedir = os.path.expanduser("~")
        dirs = homedir + '/Downloads'
        resolution = request.POST.get('resolution')
        yt.streams.get_by_resolution(resolution).download(dirs)
        return redirect('download_done')
    return render(request,'download.html', context)
    
def download_done(request):
        return render(request, 'downloaddone.html')