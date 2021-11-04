from django.db import models
from django.forms import ModelForm
from .models import Ticket, Review, UserFollows


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']


class FollowForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ['user_to_follow']