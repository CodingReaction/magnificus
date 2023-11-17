from django.shortcuts import render
from django.http import HttpRequest


def index_view(request: HttpRequest):
    search = ""
    return render(request, 'example/basics.html', context={"search": search})
