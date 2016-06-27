from django.test import TestCase
from django.core.urlresolvers import reverse


class AccountsTestCase(TestCase):
    """Test that accout sign ups are working correctly"""
    def test_student_signup(self):
        """Test that the users signup page recieves a 200 status code"""
        url = reverse('user_signup')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_teacher_signup(self):
        """Test that the teachers signup page recieves a 200 status code"""
        url = reverse('teacher_signup')
        resp = self.client.get(url)
        self.assertTrue(resp.status_code, 200)
