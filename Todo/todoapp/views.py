from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mytodo
from .forms import TodoForm

# Create your views here.
def todo(request): 
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'todo.html',{'tasks': tasks, 'form':form})

def deleteItem(request, pk):
    task = Mytodo.objects.get(id=pk)
    task.delete()
    return redirect('todo')    

def updateItem(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateform = TodoForm(instance=todo)
    if request.method == "POST":
        updateform = TodoForm(request.POST, instance= todo)
        if updateform.is_valid():
            updateform.save()
            return redirect('todo')    
    return render(request,'updateItem.html', {'todo':todo, 'updateform': updateform})        