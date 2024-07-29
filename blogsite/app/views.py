from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView
from .models import Post, BlogComment
from . import forms


def home(request):    
    posts = Post.objects.filter(is_draft=False)
    context = {"posts":posts} 
    return render(request,'allblog.html',context)


def detailBlog(request,pk):
    print('detail me aaya')
    post = Post.objects.get(pk=pk)  
    if request.method == 'POST':
        print('detail ke comment')
        name= request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        blogobj, created = BlogComment.objects.get_or_create(name=name,email=email,comment=comment,blog=post) 

    context = {
        "post":post 
    }
    return render(request,'detailarticle.html',context)  


        

# class DetailArticle(DetailView):
#     model= Post 
#     template_name = "detailarticle.html"


    
            

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


    



