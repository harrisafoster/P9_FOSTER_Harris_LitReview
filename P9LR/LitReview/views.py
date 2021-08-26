from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'LitReview/dashboard.html', {'dude': 1})


def pieces(request):
    return render(request, 'LitReview/pieces.html')


def profile(request):
    return render(request, 'LitReview/profile.html')
# Create your views here.
