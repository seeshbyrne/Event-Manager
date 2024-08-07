from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # protect view functions
from django.contrib.auth.mixins import LoginRequiredMixin # protect class based views

from .models import Event, Comment
from .forms import CommentForm, GuestForm, EventCreateForm

from django.http import JsonResponse
from django.db.models import Q 

# Home
class Home(LoginView):
    template_name = 'home.html'

# About
def about(request):
    return render(request, 'about.html')

# Sign Up
def signup(request):
    error_message = ''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event-index')
        else:
            error_message = 'Invalid login - try again'
            # this would be the last line of the post request
    # everything here runs IF we had a GET request
    # OR if the form was invalid
    context = {'form': form, 'error_messsage': error_message}
    return render(request, 'signup.html', context)

# Index - Showing all Events
@login_required
def event_index(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    if query:
        events = Event.objects.filter(
            Q(name__icontains=query) |  # Search by event name
            Q(date__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query) | # Optionally search by description
            Q(category__icontains=query)
        ).distinct()
    else:
        events = Event.objects.filter(Q(user=request.user) | Q(guests=request.user)).distinct()

    return render(request, 'events/index.html', {'events': events, 'query': query})


# Detail - Showing Individual Event
@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    # instantiate CommentForm to be rendered in the template
    comment_form = CommentForm()
    guest_form = GuestForm()
    return render(request, 'events/detail.html', {
        'event': event,
        'comment_form': comment_form,
        'guest_form': guest_form,
    })

# Create Event
class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm 
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the event
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
# Update Event
class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'

# Delete Event
class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'



# Add Comment
@login_required
def add_comment(request, event_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.event_id = event_id
        comment.user = request.user
        comment.save()
    return redirect('event-detail', event_id=event_id)

# Edit Comment
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect('event-detail', event_id=comment.event.id)

    if request.method == 'POST':
        comment.comment = request.POST['comment']
        comment.save()
        return redirect('event-detail', event_id=comment.event.id)

# Delete Comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        event_id = comment.event.id
        comment.delete()
    return redirect('event-detail', event_id=event_id)




# GUESTS
@login_required
def add_guests(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.user:
        return redirect('event-detail', event_id=event_id)

    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guests = form.cleaned_data['guests']
            event.guests.set(guests)
            return redirect('event-detail', event_id=event_id)
    else:
        invited_guests = event.guests.all()
        all_users = User.objects.exclude(id__in=invited_guests.values_list('id', flat=True))
        form = GuestForm(initial={'guests': event.guests.all()})

    return render(request, 'events/add_guests.html', {'form': form, 'event': event, 'all_users': all_users})

