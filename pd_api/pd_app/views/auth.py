from django.contrib.auth import login, authenticate
from ..forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')  # Redirect to home page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')  # Redirect to home page after successful login
        else:
            # Handle invalid login credentials
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})