from multiprocessing import context
import string
from django.shortcuts import render, redirect
from .models import Link
import uuid





# Create your views here.
def index(request):
    return render(request, 'index.html')

def redirect_url(request, url):
    code = Link.objects.filter(shortcode = url)
    if len(code) == 0:
         return render(request, 'index.html')
    context = {'link': code[0]}
    return render(request, 'redirect.html', context)

def shortner(request):
    code = uuid.uuid4().hex[:6].upper()

    if request.method == 'POST':

        long_url = request.POST['url']

        new_url = Link(url = long_url, shortcode = code)
        new_url.save()
        return render( request,'shortened.html', {'shortcode':code})

    return render(request, 'shortener.html')



