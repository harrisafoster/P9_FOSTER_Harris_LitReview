from django.db import models
from django.forms import ModelForm, Form, CharField, ValidationError
from .models import Ticket, Review
from django.contrib.auth.models import User


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']


def is_in_database(name):
    usernames = []
    for obj in User.objects.all():
        usernames.append(obj.username)
    if name not in usernames:
        raise ValidationError("User not in database")


class FollowUserForm(Form):
    user_to_follow = CharField(max_length=25, validators=[is_in_database])
