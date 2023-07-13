"""Module Docstring Goes Here"""
from django.shortcuts import render

# Create your views here.
def post_list(request):
    """Function Docstring Goes Here"""
    return render(request, 'blog/post_list.html', {})
