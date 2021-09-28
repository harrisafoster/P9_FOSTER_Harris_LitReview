from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'LitReview/dashboard.html')


def pieces(request):
    return render(request, 'LitReview/pieces.html')


def profile(request):
    ## 'if user is authenticated, grab user name and info automatically'
    return render(request, 'LitReview/profile.html')
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'LitReview/signup.html', {'form': form})