from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserAdminCreationForm

# write your views here
# this is home view appear after login only
@login_required()
def Home(request):
    return HttpResponse("Home page")

# user registration view
def register_view(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.!!!!')
            return redirect('/accounts/login/')
    return render(request, 'register.html', {'form': form})

# after login this function will work
def profile(request):
    return HttpResponse("logged in successfully")

# logout view
def logout_view(request):
    logout(request)
    return redirect('register')