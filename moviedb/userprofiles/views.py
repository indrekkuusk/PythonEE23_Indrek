from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from moviedetails.models import SavedMovie  # Import the SavedMovie model from the moviedetails app

class DashboardView(LoginRequiredMixin, ListView):
    model = SavedMovie
    template_name = 'userprofiles/dashboard.html'
    context_object_name = 'saved_movies'

    def get_queryset(self):
        # Return only the saved movies that belong to the currently logged-in user
        return SavedMovie.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        # Add profile information to the context
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        # Add any other user activities or data you want to show on the dashboard
        return context
