from django.shortcuts import render, get_object_or_404
from .models import Todo, Suggestions
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    return render(request, 'todo/index.html')

def todo(request):
    todo_list=Todo.objects.all()
    return render(request, 'todo/todolist.html', {'todo_list': todo_list})

def suggestion(request):
    suggestion_list=Suggestions.objects.all()
    return render(request, 'todo/suggestion.html', {'suggestion_list': suggestion_list})

# Detailed views below

def todolistdetail(request, id):
    todo=get_object_or_404(Todo, pk=id)
    return render(request, 'todo/todolistdetail.html', {'todo': todo})  

def suggestiondetail(request, id):
    suggestion=get_object_or_404(Suggestions, pk=id)
    return render(request, 'todo/suggestiondetail.html', {'suggestion': suggestion})    
