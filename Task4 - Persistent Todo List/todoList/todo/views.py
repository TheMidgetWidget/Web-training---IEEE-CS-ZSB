from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    items = Item.objects.all()

    form = ItemForm()

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'items': items, 'form': form}
    return render(request, 'todo/todolist.html', context)

def updateItem(request, pk):
    item = Item.objects.get(id=pk)

    form = ItemForm(instance=item)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'form': form}

    return render(request, 'todo/updateitem.html', context)

def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect("/")