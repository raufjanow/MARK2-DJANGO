from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')  

def about(request):
    return render(request, 'about.html')

def class_view(request):
    return render(request, 'class.html')

def blog(request):
    return render(request, 'blog.html')


