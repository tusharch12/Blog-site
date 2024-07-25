from django.urls import path 
from . import views

urlpatterns = [
   path('article/<int:pk>',views.DetailArticle.as_view(),name="Detail-Article"),
   path('',views.HomeView.as_view(),name = "All-blog"),
   path('add/',views.addpost,name= 'Add-post')
   # path('',views.blogEditor, name = "Add-Post")

]
