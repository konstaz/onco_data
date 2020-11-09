from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from account.models import User
from account.forms import CreateExternalUserForm, ChangePasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MyProfile(LoginRequiredMixin, UpdateView):
    template_name = 'user-edit.html'
    queryset = User.objects.all()
    fields = ('email', 'first_name', 'last_name', 'username')
    success_url = reverse_lazy('index')

    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(id=self.request.user.id)


class SignUp(CreateView):
    template_name = 'registration/user-sign-up.html'
    model = User
    success_url = reverse_lazy('index')
    form_class = CreateExternalUserForm


class ChangePassword(LoginRequiredMixin, UpdateView):
    template_name = 'password-change.html'
    model = User
    success_url = reverse_lazy('index')
    form_class = ChangePasswordForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
