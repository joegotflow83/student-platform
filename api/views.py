from rest_framework import generics, viewsets
from django.contrib.auth.models import User

from dashboard.models import Student
from .serializers import StudentSerializer, UserSerializer


class StudentsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRetrieveUpdateAPIView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    lookup_field = 'name_of_class'

    def get_queryset(self):
        Student.objects.filter(name_of_class=self.kwargs['subject'])


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
