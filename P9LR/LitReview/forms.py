from django.db import models
from django.forms import ModelForm, Form, CharField, ValidationError
from .models import Ticket, Review
from django.contrib.auth.models import User
from django import forms


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']
        choices = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
        widgets = {
            'rating': forms.RadioSelect(choices=choices)
        }


def is_in_database(name):
    if not User.objects.filter(username=name).exists():
        raise ValidationError("User not in database")


class FollowUserForm(Form):
    user_to_follow = CharField(max_length=25, validators=[is_in_database])

    def clean(self):
        clean_data = super().clean()
        return clean_data

