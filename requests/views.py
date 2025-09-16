# In your app's views.py file

from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieRequest
from django.contrib.auth.decorators import login_required


# --- View to LIST all requests ---
def index(request):
    all_requests = MovieRequest.objects.all().order_by('-date')
    template_data = {
        'title': 'All Movie Requests',
        'requests': all_requests
    }
    return render(request, 'requests/index.html', {'template_data': template_data})


# --- View to ADD a new request ---
@login_required
def add_request(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # Make sure the title is not empty
            MovieRequest.objects.create(
                user=request.user,
                title=title
            )
        return redirect('requests.index')

    # If it's a GET request, just show the form
    return render(request, 'requests/add.html')


# --- View to DELETE a request ---
@login_required
def delete_request(request, request_id):
    movie_request = get_object_or_404(MovieRequest, id=request_id)

    # Only the owner or a staff member can delete
    if request.user == movie_request.user or request.user.is_staff:
        movie_request.delete()

    return redirect('requests.index')