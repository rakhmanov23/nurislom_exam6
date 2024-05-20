from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView

from apps.forms import RegisterModelForm
# from apps.forms import RegisterModelForm, UpdateModelForm
from apps.models import User
from apps.tasks import send_to_user_email


class UserListView(ListView):
    template_name = 'apps/employers_pagination.html'
    queryset = User.objects.all()
    context_object_name = 'users'
    paginate_by = 2


class UserDetailView(DetailView):
    template_name = 'apps/detail.html'


class LoginView(TemplateView):
    template_name = 'apps/auth/log_in.html'


class RegisterView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = RegisterModelForm
    success_url = 'login/'


def form_valid(self, form):
    _id = User.objects.all().order_by('-id').first().id + 1
    send_to_user_email.delay(form.data['email'],
                             f"siz muvaffaqiyatli ro'yxatdan o'tdingiz va sizning id ingiz: {_id}  ")
    return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'apps/profile.html'


class ProfileUpdateView(UpdateView):
    template_name = 'apps/profile.html'
    fields = ["first_name", 'last_name']
