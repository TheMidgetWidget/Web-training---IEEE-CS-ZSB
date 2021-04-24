from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
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

def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print("here")
        if form.is_valid():
            print("valid")
            user = form.save()
            login(request, user)
            messages.info(request, "Registration successful." )
            return redirect("/")
        else:
            messages.info(request, 'Oops! something went wrong...')
    form = RegisterForm
    context = {"form":form}
    return render(request, 'register.html', context)

def loginUser(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("/")
			else:
				messages.info(request,"Invalid username or password.")
		else:
			messages.info(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})

def logoutUser(request):
    logout(request)
    return redirect("/")