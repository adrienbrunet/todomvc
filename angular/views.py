# coding: utf-8

# Adrien Brunet <brunet.adrien@gmail.com>


from django.shortcuts import render


def todo_angular(request):
    return render(request, 'angular-todo.html', {})
