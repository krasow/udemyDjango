from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html', {})
