from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView
from .models import Post
from . import forms


class HomeView(ListView):
    model = Post 
    template_name = "allblog.html"

class DetailArticle(DetailView):
    model= Post 
    template_name = "detailarticle.html"

def addpost(request):

    form = forms.Blogform()
    print(form)
    if request.method == 'POST':
        form = forms.Blogform(request.POST)
        if(form.is_valid):
            form.save() 
            form = forms.Blogform
    context = {"form":form} 
    return render(request,'add_post.html',context)       


    



