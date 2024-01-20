
from django.test import TestCase
from users.models import User
from sport_events.models import SportEvent
from .serializers import UserAddSerializer, SportEventSerializer, SportEventAddSerializer

class SerializerTests(TestCase):
    def setUp(self):
        self.user_data = {'username': 'testuser', 'password': 'testpass', 'email': 'test@example.com', 'phoneNumber': '123456789'}
        self.sport_event_data = {'host': self.user_data, 'sport_type': 'Football', 'date': '2024-01-20', 'ora': '12:00:00', 'locatie': 'Stadium', 'status': False, 'limit_capacity': 100}

    def test_user_add_serializer(self):
        serializer = UserAddSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, self.user_data)

    def test_sport_event_serializer(self):
        user = User.objects.create(**self.user_data)
        serializer_data = {**self.sport_event_data, 'host': user}
        serializer = SportEventSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())

    def test_sport_event_add_serializer(self):
        serializer = SportEventAddSerializer(data=self.sport_event_data)
        self.assertFalse(serializer.is_valid())

