from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from toDo.forms import TodoForm
from toDo.models import Todo

# Create your views here.

@login_required
def todo_list(request):
    data = Todo.objects.filter(user = request.user)
    context = {
        'data':data
    }
    return render(request,'toDos/todo_list.html',context)

@login_required
def todo_detail(request,id):
    data = Todo.objects.get(id = id)
    context = {
        'data':data
    }
    return render(request,'toDos/todo_details.html',context)

@login_required
def todo_create(request):
    if request.method == "POST":
        form  = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            return redirect('list_html')
    else:
        form = TodoForm()
    context = {
        'form':form
    }
    return render(request,'toDos/todo_form.html',context)

@login_required
def todo_update(request,id):
    data = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm(instance=data)
    
    context = {
        'form':form
    }
    return render(request,'toDos/todo_form.html',context)


@login_required
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list_html')
    context = {
        'todo': todo
    }
    return render(request, 'toDos/todo_confirm.html', context)

@login_required
def todo_toggle(request,id):
    data = Todo.objects.get(id=id)

    if data.status=='pending':
        data.status = 'complete'
    else:
        data.status = 'pending'
    data.save()
    return redirect('list_html')



