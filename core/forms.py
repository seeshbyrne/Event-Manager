from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class GuestForm(forms.Form):
    guests = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)




class InviteGuestForm(forms.Form):
    email = forms.EmailField(label='Guest Email', max_length=254)