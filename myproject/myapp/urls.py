from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'), 
#     path('index.html', views.index, name='index'), 
#     path('about.html', views.about, name='about'),
#     path('class.html', views.class_view, name='class'),
#     path('blog.html', views.blog, name='blog'),
# ]

#                                            SECOND WAY
from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name ='about'),
    path('blog/',views.blog,name ='blog'),
    path('class/',views.clas,name ='class'),
    path('',views.copy_blog_fun,name="index"),
    # path('mark',views.copy_li_fun,name="mark")
]


