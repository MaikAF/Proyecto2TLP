from django.shortcuts import render

def home(request):
    return render(request, 'miapp/base.html', name='base')