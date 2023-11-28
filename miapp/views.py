from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    data = {
        'title': 'Inicio',
    }

    return render(request, 'templates/base.html', data)