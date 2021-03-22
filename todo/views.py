from django.shortcuts import render
from .models import Todo, Suggestions

# Create your views here.
def index (request):
    return render(request, 'todo/index.html')

def todo(request):
    todo_list=Todo.objects.all()
    return render(request, 'todo/todolist.html', {'todo_list': todo_list})

def suggestion(request):
    suggestion_list=Suggestions.objects.all()
    return render(request, 'todo/suggestion.html', {'suggestion_list': suggestion_list})
