from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import UserProfile


class UserSignup(CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        UserProfile.objects.create(pk=new_user.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class TeacherSignup(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'auth/teacher_form.html'

    def form_valid(self, form):
        new_teacher = form.save(commit=False)
        UserProfile.objects.create(pk=new_teacher.pk, teacher=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')
