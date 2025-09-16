# In your app's urls.py file

from django.urls import path
from . import views

urlpatterns = [
    # Shows the list of all movie requests
    path('requests/', views.requests_index, name='requests.index'),

    # Shows the form to add a new request and handles submission
    path('requests/add/', views.add_request, name='requests.add'),

    # Handles the deletion of a specific request
    path('requests/<int:request_id>/delete/', views.delete_request, name='requests.delete'),

    # ... include any other URLs you have ...
]