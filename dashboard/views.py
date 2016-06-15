from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Class


class Dashboard(TemplateView):
    """Dashboard for teachers and students"""
    template_name = 'dashboard/dashboard.html'


class CreateClass(CreateView):
    """Teachers can create classes"""
    model = Class
    fields = '__all__'

    def get_success_url(self):
        return reverse('dashboard')
