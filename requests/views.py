from django.shortcuts import render
from .models import MovieRequest # Import the MovieRequest model

def index(request):
    """
    This view fetches all existing movie requests from the database
    and displays them on a page.
    """
    # Query the database to get all MovieRequest objects
    all_requests = MovieRequest.objects.all().order_by('-date') # Orders by newest first

    template_data = {}
    template_data['title'] = 'All Movie Requests'
    template_data['requests'] = all_requests

    # It's a good practice to use a separate template for requests
    return render(request, 'requests/index.html',
                  {'template_data': template_data})