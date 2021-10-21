from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from django.views.generic import ListView, UpdateView, DeleteView
import operator
from django.urls import reverse


def login_page(request):
    if request.user.is_authenticated:
        return redirect('flux')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('flux')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('flux')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('flux')
        else:
            form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect('login_page')


class PostListView(ListView):
    # example includes a view based on functions to combine models
    template_name = 'LitReview/flux.html'
    context_object_name = 'list_reviews'

    def get_queryset(self):
        return Ticket.objects.order_by('-time_created')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['responses'] = Review.objects.order_by('-time_created')
        pks = []
        for obj in Review.objects.all():
            pks.append(obj.ticket.pk)
        context['pks'] = pks
        return context


class PersonalPostListView(ListView):
    model = Ticket
    template_name = 'LitReview/posts.html'
    context_object_name = 'list_reviews'

    def get_queryset(self):
        personal_posts = Ticket.objects.filter(user=self.request.user)
        return sorted(personal_posts, key=operator.attrgetter('time_created'), reverse=True)


class UpdatePostView(UpdateView):
    model = Ticket
    template_name = 'LitReview/edit_ticket.html'
    fields = ['title', 'description', 'image']

    def get_success_url(self):
        return reverse('posts')


class DeletePostView(DeleteView):
    model = Ticket
    template_name = 'LitReview/delete_ticket.html'

    def get_success_url(self):
        return reverse('posts')


def edit_review(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    context = {}
    return render(request, 'LitReview/edit_review.html', context)


def create_ticket(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    context = {'form': form}
    return render(request, 'LitReview/create_ticket.html', context)


def create_response(request, pk):
    # form that contains both models or inherits one model into another, not necessary to use the models to create the forms
    if not request.user.is_authenticated:
        return redirect('login_page')
    ticket = Ticket.objects.get(pk=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    context = {'form': form, 'ticket': ticket}
    return render(request, 'LitReview/create_response.html', context)


def create_review(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    context = {}
    return render(request, 'LitReview/create_review.html', context)


def subscriptions(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    context = {}
    return render(request, 'LitReview/subscriptions.html', context)
