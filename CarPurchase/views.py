from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    context = {
        "form": UserRegistrationForm()
    }
    return render(request, 'register.html', context)
