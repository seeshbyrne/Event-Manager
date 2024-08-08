from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar'),
    path('events/<int:event_id>/add_guests/', views.add_guests, name='add-guests'),

    path('events/', views.event_index, name='event-index'),
    path('events/<int:event_id>/', views.event_detail, name='event-detail'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),

    path('events/<int:event_id>/add_comment/', views.add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),

]