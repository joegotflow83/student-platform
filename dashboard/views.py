from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.db.models import Q

from .models import Class, Schedule, Student, Announcement, File
from .forms import FileForm


class Dashboard(TemplateView):
    """Dashboard for teachers and students"""
    template_name = 'dashboard/dashboard.html'


class CreateClass(CreateView):
    """Teachers can create classes"""
    model = Class
    template_name = 'dashboard/teacher/class_form.html'
    fields = ['name', 'level', 'credits', 'location', 'start_date', 'end_date', 'start_time', 'end_time', 'limit']

    def form_valid(self, form):
        new_class = form.save(commit=False)
        new_class.user = self.request.user
        new_class.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


class StudentListClasses(ListView):
    """Display classes that the student to take"""
    model = Class
    template_name = 'dashboard/student/class_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = Schedule.objects.get(user=self.request.user)
        for course in Class.objects.all():
            for _class in schedule.classes.all():
                if course == _class:
                    context['has_course'] = True
                    print(context['has_course'])
            else:
                context['has_course'] = False
                print(context['has_course'])
                return context
        return context


class TeacherListClasses(ListView):
    """Display classes that the teacher has created"""
    model = Class
    template_name = 'dashboard/teacher/teacher_classlist.html'

    def get_queryset(self):
        return Class.objects.filter(user=self.request.user)


class AddClass(View):
    """Allow a student to enroll in a class"""
    def get(self, request, pk):
        _class = Class.objects.get(pk=pk)
        new_student = Student(user=request.user, name_of_class=_class.name)
        new_student.save()
        _class.students.add(new_student)
        schedule = Schedule.objects.get(user=request.user)
        schedule.classes.add(_class)
        _class.taken += 1
        _class.save()
        return redirect('dashboard')


class RemoveClass(View):
    """Allow a student to drop a class"""
    def get(self, request, class_pk, student_pk):
        _class = Class.objects.get(pk=class_pk)
        student = Student.objects.get(Q(user=student_pk), Q(name_of_class=_class.name))
        _class.students.remove(student)
        schedule = Schedule.objects.get(user=request.user)
        schedule.classes.remove(_class)
        student.delete()
        _class.taken -= 1
        _class.save()
        return redirect('dashboard')


class ViewStudentClasses(TemplateView):
    """Display all the classes the student is enrolled in"""
    template_name = 'dashboard/student/schedule_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = Schedule.objects.get(user=self.request.user)
        context['classes'] = schedule.classes.all()
        return context


class TeacherClassDetail(DetailView):
    """Details about a specific class from teachers side"""
    model = Class
    template_name = 'dashboard/teacher/class_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Class.objects.get(pk=self.kwargs['pk'])
        context['students'] = subject.students.all()
        return context


class StudentClassDetail(DetailView):
    """Details about a specific class from students side"""
    model = Class
    template_name = 'dashboard/student/class_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcements'] = Announcement.objects.filter(_class=self.kwargs['pk']).order_by('-created')
        context['files'] = File.objects.filter(_class=self.kwargs['pk']).order_by('-created')
        return context


class CreateAnnouncement(CreateView):
    """Teachers can create announcements for their classes"""
    model = Announcement
    fields = ('title', 'body')
    template_name = 'dashboard/teacher/announcement_form.html'

    def form_valid(self, form):
        new_announcement = form.save(commit=False)
        new_announcement.user = self.request.user
        _class = Class.objects.get(pk=self.kwargs['pk'])
        new_announcement._class = _class
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('teacher_course_detail', kwargs={'pk': self.kwargs['pk']})


class UploadFile(FormView):
    model = File
    template_name = 'dashboard/teacher/upload_file.html'
    form_class = FileForm

    def form_valid(self, form):
        new_file = form.save(commit=False)
        _class = Class.objects.get(pk=self.kwargs['pk'])
        new_file._class = _class
        new_file.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('teacher_course_detail', kwargs={'pk': self.kwargs['pk']})
