from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main page opened WTF')

def group_posts(request, slug):
    return HttpResponse('Группы группки группоньки')
