from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from .serializers import UserSerializer


class APITest(APITestCase):
    """Test apis"""
    def setUp(self):
        self.data = {'username': 'joe'}

    def test_all_students_api(self):
        """Test that all students display"""
        resp = self.client.get(reverse('list_create_students'))
        self.assertTrue(resp.status_code, 200)

    def test_student_class_name_api(self):
        """Test that all classes with inputted name display"""
        resp = self.client.get(reverse('student_class_name', args=['Math']))
        self.assertTrue(resp.status_code, 200)

    def test_get_users_api(self):
        """Test that all users display"""
        resp = self.client.get(reverse('list_create_users'))
        self.assertTrue(resp.status_code, 200)

    def test_post_users_api(self):
        """Test that post method works"""
        data = {'username': 'joe'}
        resp = self.client.post(reverse('list_create_users'), data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_put_users_api(self):
        """Test that put method works"""
        user = User.objects.create(username='joe')
        data = UserSerializer(user).data
        data.update({'username': 'joseph'})
        resp = self.client.put(reverse('retrieve_update_destroy_user', args=[user.pk]), data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_destroy_uses_api(self):
        """Test that destory method works"""
        user = User.objects.create(username='joe')
        resp = self.client.delete(reverse('retrieve_update_destroy_user', args=[user.pk]))
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_single_user_api(self):
        """Test that a single user is displayed"""
        user = User.objects.create(username='joe')
        resp = self.client.get(reverse('retrieve_update_destroy_user', args=[user.pk]))
        self.assertTrue(resp.status_code, 200)
