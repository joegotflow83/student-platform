from django.test import TestCase


class AccountsTestCase(TestCase):
    """Test that accout sign ups are working correctly"""
    def test_student_signup(self):
        """Test that the users signup page recieves a 200 status code"""
        resp = self.client.get('accounts/student_signup')
        self.assertEqual(resp.status_code, 200)
