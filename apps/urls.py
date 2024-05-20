from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import TemplateView

from apps.views import ProfileView, ProfileUpdateView, UserListView, UserDetailView, RegisterView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile_page'),
    path('employer/', UserListView.as_view(), name='employer_page'),
    path('detail/<int:pk>/', UserDetailView.as_view, name='detail_page'),
    path('login/', LoginView.as_view(
        template_name='apps/auth/log_in.html',
        next_page='employer_page',
        redirect_authenticated_user=True
    ), name='login_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update-page')
]
