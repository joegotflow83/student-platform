from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from dashboard.models import Student, Announcement, Class
from .serializers import StudentSerializer, UserSerializer, AnnouncementSerializer, ClassSerializer


class StudentsListCreateAPIView(generics.ListCreateAPIView):
    """All students endpoint"""
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentNameClassAPIView(viewsets.ModelViewSet):
    """All students in a particular class andpoint"""
    serializer_class = StudentSerializer
    lookup_field = 'name_of_class'

    def get_queryset(self):
        return Student.objects.filter(name_of_class=self.kwargs['subject'])


class UsersListCreateAPIView(generics.ListCreateAPIView):
    """All users endpoint"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Single user endpoint"""
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])


class AnnouncementsListCreateAPIView(generics.ListCreateAPIView):
    """All announcements endpoint"""
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return super().create(request, *args, **kwargs)


class AnnouncementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Single announcement endpoit"""
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        return Announcement.objects.filter(pk=self.kwargs['pk'])


"""class AnnouncementsViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()"""


class ClassesViewSet(viewsets.ViewSet):
    """All classes enpoint"""
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
