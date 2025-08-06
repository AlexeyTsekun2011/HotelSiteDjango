from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout,get_user
from .forms import CustomUserCreationForm,CustomUserLoginForm,BookingForm
from .models import Room
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {"form": form})


def user_login(request): #*
    if request.method == 'POST':
        form = CustomUserLoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {"form":form})


def room(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request,'room_detail.html',{'room':room})


def home(request):
    rooms = Room.objects.all()
    query_type = request.GET.get('type')
    query_price = request.GET.get('max_price')
    if query_type:
        rooms = rooms.filter(type=query_type)


    if query_price:
        rooms = rooms.filter(price__lte=query_price)
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required
def book_room(request,room_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user
            saved_form = form.save(commit=False)
            saved_form.user = user
            saved_form.save()
            return redirect('book')
    else:
        form = BookingForm()
    return render(request, 'book_room.html',{"form": form})




