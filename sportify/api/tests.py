from django.test import TestCase
from users.models import User
from sport_events.models import SportEvent
from rest_framework import serializers
from api.serializers import UserSerializer, UserAddSerializer, SportEventSerializer, SportEventAddSerializer
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from users.models import User

class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user_data = {'id': 1, 'username': 'testuser', 'password': 'testpass', 'email': 'test@example.com', 'phoneNumber': '123456789'}
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, user_data)

    def test_user_add_serializer(self):
        user_data = {'username': 'testuser', 'password': 'testpass', 'email': 'test@example.com', 'phoneNumber': '123456789'}
        serializer = UserAddSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, user_data)

class SportEventSerializerTest(TestCase):
    def test_sport_event_serializer(self):
        sport_event_data = {'id': 1, 'host': 'testhost', 'sport_type': 'Football', 'date': '2024-01-20', 'ora': '12:00:00', 'locatie': 'Stadium', 'status': False, 'limit_capacity': 100}
        serializer = SportEventSerializer(data=sport_event_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, sport_event_data)

    def test_sport_event_add_serializer(self):
        sport_event_data = {'host': 'testhost', 'sport_type': 'Football', 'date': '2024-01-20', 'ora': '12:00:00', 'locatie': 'Stadium', 'status': False, 'limit_capacity': 100}
        serializer = SportEventAddSerializer(data=sport_event_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, sport_event_data)

class UserViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='testpassword', email='testuser@example.com')

    def test_user_list_view(self):
        url = reverse('user_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail_view(self):
        url = reverse('user_detail', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SportEventViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.sport_event = SportEvent.objects.create(
            host='testuser',
            sport_type='Football',
            date='2024-01-20',
            ora='12:00:00',
            locatie='Stadium',
            status=False,
            limit_capacity=100
        )

    def test_sport_event_list_view(self):
        url = reverse('sport_event_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sport_event_detail_view(self):
        url = reverse('sport_event_detail', args=[self.sport_event.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

