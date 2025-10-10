from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def frontpage(request):
    return render(request,"web/frontpage.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form= UserCreationForm()
    return render(request, 'web/signup.html',{'form':form})    

