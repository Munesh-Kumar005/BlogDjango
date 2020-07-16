
from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_header = "Munesh Admin"
admin.site.site_title = "Munesh Admin Portal"
admin.site.index_title = "Welcome to Munesh Blog Portal"



urlpatterns = [
    #api post comment
    path('postComment', views.postComment, name='postComment'),
    path('', views.blogHome, name='bloghome'),
    path('<str:slug>', views.blogPost, name='blogpost'),
    
   
   
]
