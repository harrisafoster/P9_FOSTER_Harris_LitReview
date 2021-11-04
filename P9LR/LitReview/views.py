from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from django.views.generic import ListView
import operator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


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
    template_name = 'LitReview/flux.html'
    context_object_name = 'list_tickets'

    def get_queryset(self):
        return Ticket.objects.order_by('-time_created')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.order_by('-time_created')
        pks = []
        for obj in Review.objects.all():
            pks.append(obj.ticket.pk)
        context['pks'] = pks
        return context


class PersonalPostListView(ListView):
    template_name = 'LitReview/my_posts.html'
    context_object_name = 'list_tickets'

    def get_queryset(self):
        personal_reviews = Review.objects.filter(user=self.request.user)
        reviewed_posts = []
        for review in personal_reviews:
            reviewed_posts.append(review.ticket)
        personal_tickets = list(Ticket.objects.filter(user=self.request.user))
        for post in reviewed_posts:
            if post not in personal_tickets:
                personal_tickets.append(post)
        return sorted(personal_tickets, key=operator.attrgetter('time_created'), reverse=True)

    def get_context_data(self, **kwargs):
        context = super(PersonalPostListView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.order_by('-time_created')
        return context


@login_required(redirect_field_name='login_page')
def edit(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    try:
        review = Review.objects.get(ticket=ticket)
    except ObjectDoesNotExist:
        review_pk = 0
    else:
        review_pk = review.pk

    if review_pk != 0:
        review = Review.objects.get(ticket=ticket)
        if review.user == request.user and ticket.user == request.user:
            return edit_review_and_ticket(request, review_pk=review_pk, ticket_pk=ticket.pk)
    if ticket.user == request.user:
        return edit_ticket(request, pk=ticket.pk)
    else:
        return edit_review(request, review_pk=review_pk, ticket_pk=ticket.pk)


@login_required(redirect_field_name='login_page')
def edit_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    form = TicketForm(instance=ticket)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            return redirect('my_posts')
    context = {'form': form}
    return render(request, 'LitReview/edit_ticket.html', context)


@login_required(redirect_field_name='login_page')
def edit_review(request, review_pk, ticket_pk):
    ticket = Ticket.objects.get(pk=ticket_pk)
    review = Review.objects.get(pk=review_pk)
    form = ReviewForm(instance=review)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('my_posts')
    context = {'form': form, 'ticket': ticket}
    return render(request, 'LitReview/edit_review.html', context)


@login_required(redirect_field_name='login_page')
def edit_review_and_ticket(request, review_pk, ticket_pk):
    ticket = Ticket.objects.get(pk=ticket_pk)
    review = Review.objects.get(pk=review_pk)
    form1 = TicketForm(instance=ticket)
    form2 = ReviewForm(instance=review)
    if request.method == "POST":
        form1 = TicketForm(request.POST, request.FILES, instance=ticket)
        if form1.is_valid():
            ticket = form1.save(commit=False)
            ticket.save()
        form2 = ReviewForm(request.POST, instance=review)
        if form2.is_valid():
            review = form2.save(commit=False)
            review.save()
            return redirect('my_posts')
    context = {'form1': form1, 'form2': form2}
    return render(request, 'LitReview/edit_review_and_ticket.html', context)


@login_required(redirect_field_name='login_page')
def delete(request, pk):
    #all error handling and redirection to editing pages should be done here. Figure out of functions work better than classes.
    ticket = Ticket.objects.get(pk=pk)
    try:
        review = Review.objects.get(ticket=ticket)
    except:
        pass


@login_required(redirect_field_name='login_page')
def delete_review(request):
    context = {}
    return render(request, 'LitReview/delete_review.html', context)


@login_required(redirect_field_name='login_page')
def delete_ticket(request):
    context = {}
    return render(request, 'LitReview/delete_ticket.html', context)


@login_required(redirect_field_name='login_page')
def delete_review_and_ticket(request):
    context = {}
    return render(request, 'LitReview/delete_review_and_ticket.html', context)


@login_required(redirect_field_name='login_page')
def create_ticket(request):
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


@login_required(redirect_field_name='login_page')
def create_response(request, pk):
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


@login_required(redirect_field_name='login_page')
def create_review(request):
    form1 = TicketForm()
    form2 = ReviewForm()
    if request.method == "POST":
        form1 = TicketForm(request.POST, request.FILES)
        form2 = ReviewForm(request.POST)
        if form1.is_valid():
            ticket = form1.save(commit=False)
            ticket.user = request.user
            ticket.save()
        ref_list = []
        for obj in Ticket.objects.all():
            ref_list.append(obj.pk)
        if form2.is_valid():
            review = form2.save(commit=False)
            review.user = request.user
            review.ticket = Ticket.objects.get(pk=ref_list[-1])
            review.save()
            return redirect('flux')
    context = {'form1': form1, 'form2': form2}
    return render(request, 'LitReview/create_review.html', context)


@login_required(redirect_field_name='login_page')
def subscriptions(request):
    context = {}
    return render(request, 'LitReview/subscriptions.html', context)
