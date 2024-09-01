from django.urls import path
from .views import view_profile, update_profile

urlpatterns = [
    path('profile/', view_profile, name='view_profile'),
    path('profile/update/', update_profile, name='update_profile'),
    # path('dashboard/', DashboardView.as_view(), name='user_dashboard'),
]
