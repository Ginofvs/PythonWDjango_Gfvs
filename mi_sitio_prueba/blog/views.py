from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all() # este posts = Post.objects.all()
    # obtiene tdas las publicaciones de la bd
    return render(request,'blog/home.html',{ 'posts' : posts}) # para renderizar la plantilla con las publicaciones ? 
