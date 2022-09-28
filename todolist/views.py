import datetime
from todolist.models import TodoList
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = TodoList.objects.filter(user=request.user)
    context = {
        'list': data_todolist,
        'username': request.user.username,
        'daftar_task': data_todolist,
    }
    return render(request, 'todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('latest_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('latest_login')
    return response

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TodoList.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    return render(request,"create_task.html")

@login_required(login_url='login/')
def update_task(request, id):
    task = TodoList.objects.get(id=id)
    if task.user == request.user:
        task.is_finished ^= True
    else:
        return redirect('todolist:show_todolist')
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='login/')
def delete_task(request, id):
    task = TodoList.objects.get(id=id)
    if task.user == request.user:
        task.delete()
    else:
        return redirect('todolist:show_todolist')
    return redirect('todolist:show_todolist')