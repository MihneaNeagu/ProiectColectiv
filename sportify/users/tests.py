from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'testpassword')

    def test_unique_username_constraint(self):
        duplicate_user = User(username='testuser', password='anotherpassword')
        with self.assertRaises(Exception):
            duplicate_user.save()

    def test_null_username_constraint(self):
        user_with_null_username = User(username=None, password='testpassword')
        with self.assertRaises(Exception):
            user_with_null_username.save()

    def test_null_password_constraint(self):
        user_with_null_password = User(username='testuser', password=None)
        with self.assertRaises(Exception):
            user_with_null_password.save()
