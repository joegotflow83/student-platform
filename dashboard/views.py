from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from .models import Class, Schedule


class Dashboard(TemplateView):
    """Dashboard for teachers and students"""
    template_name = 'dashboard/dashboard.html'


class CreateClass(CreateView):
    """Teachers can create classes"""
    model = Class
    fields = '__all__'

    def get_success_url(self):
        return reverse('dashboard')


class ListClasses(ListView):
    """Display classes that the student to take"""
    model = Class


class AddClass(View):
    """Allow a student to enroll in a class"""
    def get(self, request, pk):
        _class = Class.objects.get(pk=pk)
        schedule = Schedule.objects.get(user=request.user)
        schedule.classes.add(_class)
        return redirect('dashboard')


class ViewStudentClasses(TemplateView):
    """Display all the classes the student is enrolled in"""
    template_name = 'dashboard/schedule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = Schedule.objects.get(user=self.request.user)
        context['classes'] = schedule.classes.all()
        return context
