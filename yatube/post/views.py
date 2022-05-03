from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text' : text,
    }
    return render(request, template, context, slug)

def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text' : text,
    }
    return render(request, template, context)

def header(request):
    template = 'includes/header.html'
    return render(request, template)

def footer(request):
    template = 'includes/footer.html'
    return render(request, template)
