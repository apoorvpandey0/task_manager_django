from django.http import HttpResponse
from django.shortcuts import  redirect, render

from todoapp.forms import TodoItemForm

# From the same folder and from models.py file import the todoapp class or function
from .models import TodoItem

def homeview(request):

    items = TodoItem.objects.all()
    completed  = TodoItem.objects.filter(completed=True)
    

    if request.method == 'POST':
        # Create a form object using the data sent by the client over POST request
        form = TodoItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    form = TodoItemForm()

    context = {
        'todoitems': items,
        'completed': completed,
        'forms':form,
    }

    # return HttpResponse('Hello World')
    return render(request, 'todoapp/index.html', context)


def removeview(request,item_id):
    # item = TodoItem.objects.get(id=item_id)

    item = TodoItem.objects.filter(id=item_id)
    if item!=None:
        item.delete()
    return redirect('home')


def aboutview(request):
    # return HttpResponse('This is my about page')
    return render(request, 'todoapp/about.html')

def completeview(request,item_id):
    item = TodoItem.objects.get(id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('home')

def htmldemoview(request):
    return render(request,'todoapp/demo.html')