from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from dashboard.models import Student, Announcement
from .serializers import StudentSerializer, UserSerializer, AnnouncementSerializer


class StudentsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentNameClassAPIView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    lookup_field = 'name_of_class'

    def get_queryset(self):
        return Student.objects.filter(name_of_class=self.kwargs['subject'])


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])


class AnnouncementsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
