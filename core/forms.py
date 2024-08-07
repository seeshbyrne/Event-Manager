from django import forms
from .models import Comment, Event
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class GuestForm(forms.Form):
    guests = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

class InviteGuestForm(forms.Form):
    email = forms.EmailField(label='Guest Email', max_length=254)

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description', 'guests', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter the event name',
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter the location',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter a brief description of the event',
                'rows': 4,
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'guests': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check'
            }),
        }