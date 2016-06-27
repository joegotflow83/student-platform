from django.test import TestCase
from django.contrib.auth.models import User

from .models import Student


class ModelTest(TestCase):
    """Test that the models correctly save data"""
    def setUp(self):
        self.user = User.objects.create(username='joe', password='pass')

    def tearDown(self):
        self.user = None

    def test_student_creation(self):
        """Test student object is created successfully"""
        student = Student.objects.create(user=self.user, name_of_class="Math")
        self.assertTrue(isinstance(student, Student))
        self.assertEqual(student.__str__(), student.name_of_class)

