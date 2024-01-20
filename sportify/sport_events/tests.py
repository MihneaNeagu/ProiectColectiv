from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import SportEvent
from .constants import TIP_SPORT, DATE

User = get_user_model()

class SportEventModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_sport_event_creation(self):
        # Test that the SportEvent is created successfully
        sport_event = SportEvent.objects.create(
            username='testuser',
            sport_type='Football',
            date='2024-01-20',
            ora='12:00:00',
            locatie='Stadium',
            status=False,
            limit_capacity=100
        )

        self.assertEqual(sport_event.username, 'testuser')
        self.assertEqual(sport_event.sport_type, 'Football')
        self.assertEqual(sport_event.date, '2024-01-20')
        self.assertEqual(str(sport_event.ora), '12:00:00')
        self.assertEqual(sport_event.locatie, 'Stadium')
        self.assertFalse(sport_event.status)
        self.assertEqual(sport_event.limit_capacity, 100)

    def test_sport_event_str_method(self):
        # Test the __str__ method of the SportEvent model
        sport_event = SportEvent.objects.create(
            username='testuser',
            sport_type='Basketball',
            date='2024-01-21',
            ora='15:30:00',
            locatie='Arena',
            status=True,
            limit_capacity=50
        )
        expected_str = f"testuser, Basketball, 2024-01-21, 15:30:00, Arena, True, 50"
        self.assertEqual(str(sport_event), expected_str)

    def test_sport_type_choices(self):
        # Test that the sport_type field uses the correct choices
        sport_event = SportEvent.objects.create(
            username='testuser',
            sport_type='BOX',
            date='2024-01-22',
            ora='18:45:00',
            locatie='Court',
            status=False,
            limit_capacity=75
        )
        choices = dict(TIP_SPORT)
        self.assertIn(sport_event.sport_type, choices)

