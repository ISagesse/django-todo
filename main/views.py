from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    context = {
        'tasks': Todo.objects.order_by('-created_at')
    }
    return render(request, 'main/index.html', context)

def add(request):
    this_task = request.POST['task']
    if request.method == 'POST':
        Todo.objects.create(text=this_task)
        return redirect('/')


def delete(request, id):
    this_task = Todo.objects.get(id=id)
    this_task.delete()
    return redirect('/')
