from django.test import TestCase
from users.models import User

class TestAppModels(TestCase):
    def test_model_str(self):
        user = User.objects.create(username="John", password="somepassword")
        expected_str = f"{user.id}, {user.username}, {user.password}"
        self.assertEqual(str(user), expected_str)
