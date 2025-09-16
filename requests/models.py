from django.db import models
from django.contrib.auth.models import User

# Model for users to request new movies
class MovieRequest(models.Model):
    """
    Represents a user's request for a new movie to be added.
    """
    # Define choices for the status field for better data integrity
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, help_text="The title of the movie being requested.")
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional: Add any details like year, director, or why you want this movie."
    )

    # Foreign key linking the request to the user who made it
    # If a User is deleted, all their movie requests will also be deleted.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='movie_requests'  # Good practice for reverse lookups
    )

    def __str__(self):
        """
        String representation of the MovieRequest model.
        """
        return f"{self.title} (Requested by: {self.user.username}) - {self.get_status_display()}"
