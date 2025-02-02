from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo
from django.views import generic


class ListTodoView(generic.ListView):
    """
    Представления для списка задач
    """
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    queryset = Todo.objects.all().order_by('-create_at')


def todo_list(request):
    """
    Представления для списка задач
    """
    todo = Todo.objects.all().order_by('-create_at')
    return render(request, "marketplace/product_list.html", 
                  {"todo": todo})


def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)
    return redirect('todo:todo_list')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todo:todo_list')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    is_completed = request.POST.get('isCompleted', False)
    if is_completed == 'on':
        is_completed = True

    todo.is_completed = is_completed
    todo.save()
    return redirect('todo:todo_list')
