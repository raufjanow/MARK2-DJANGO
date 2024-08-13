from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')

# def home(request):
#     return render(request, 'index.html')  

# def about(request):
#     return render(request, 'about.html')

# def class_view(request):
#     return render(request, 'class.html')

# def blog(request):
#     return render(request, 'blog.html')



#                                            SECOND WAY

def index(request):
    return render (request,'index.html')


def index(request):
    menu_items = [
        {"name": "Home", "url": "index", "active": True},
        {"name": "About", "url": "about", "active": False},
        {"name": "Classes", "url": "classes", "active": False},
        {"name": "Blog", "url": "blog", "active": False},
        
    ]
    return render(request, 'index.html', {'menu_items': menu_items})
