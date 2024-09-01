# userprofiles/views.py
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileUpdateForm
from moviedetails.models import SavedMovie  # Import the SavedMovie model from the moviedetails app



@login_required
def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'userprofiles/profile.html', {'profile': profile})


@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'userprofiles/update_profile.html', {'form': form})


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
