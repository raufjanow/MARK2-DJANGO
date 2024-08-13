from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('index.html', views.index, name='index'), 
    path('about.html', views.about, name='about'),
    path('class.html', views.class_view, name='class'),
    path('blog.html', views.blog, name='blog'),
]



