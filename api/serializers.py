from rest_framework import serializers
from django.contrib.auth.models import User

from dashboard.models import Student, Announcement, Class


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'users', 'name_of_class')
        lookup_field = 'name_of_class'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
