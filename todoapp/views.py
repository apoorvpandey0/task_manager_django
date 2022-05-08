from django.http import HttpResponse
from django.shortcuts import  redirect, render
from django.contrib.auth.decorators import login_required

from todoapp.forms import TodoItemForm, UserRegisterForm

# From the same folder and from models.py file import the todoapp class or function
from .models import TodoItem

def register_view(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('users-login')
    else :
        form=UserRegisterForm()
    context={
        "form":form,
        "title":"Register"
    }
    return render(request,'todoapp/register.html',context)



@login_required(login_url='/login/')
def homeview(request):

    items = TodoItem.objects.filter(user=request.user)
    completed  = TodoItem.objects.filter(completed=True,user=request.user)
    

    if request.method == 'POST':
        # Create a form object using the data sent by the client over POST request
        form = TodoItemForm(request.POST)
            
        if form.is_valid():
            # add current user to form
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
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