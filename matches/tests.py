from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils.timezone import now, timedelta
from matches.models import Match
from events.models import Event
from teams.models import Team
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class MatchModelTestCase(TestCase):
    """
    Test cases for Match model validations and methods.
    """

    def setUp(self):
        self.event = Event.objects.create(
            name="Test Event",
            description="Test Description",
            start_date="2025-01-01",
            end_date="2025-01-10"
        )
        self.team1 = Team.objects.create(name="Team 1", description="Description 1")
        self.team2 = Team.objects.create(name="Team 2", description="Description 2")

    def test_valid_match_creation(self):
        """
        Test that a valid match is created successfully.
        """
        match = Match.objects.create(
            event=self.event,
            team1=self.team1,
            team2=self.team2,
            scheduled_time=now() + timedelta(days=1),
            status="upcoming"
        )
        self.assertEqual(str(match), "Team 1 vs Team 2 (upcoming)")

    def test_invalid_same_team_match(self):
        """
        Test that a match cannot have the same team for both sides.
        """
        with self.assertRaises(ValidationError):
            Match.objects.create(
                event=self.event,
                team1=self.team1,
                team2=self.team1,
                scheduled_time=now() + timedelta(days=1),
                status="upcoming"
            )

    def test_invalid_past_scheduled_time(self):
        """
        Test that a match cannot be scheduled in the past.
        """
        with self.assertRaises(ValidationError):
            Match.objects.create(
                event=self.event,
                team1=self.team1,
                team2=self.team2,
                scheduled_time=now() - timedelta(days=1),
                status="upcoming"
            )


class MatchAPITestCase(TestCase):
    """
    Test cases for Match API endpoints.
    """

    def setUp(self):
        self.client = APIClient()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        self.client.force_authenticate(user=self.admin_user)  # Authenticate as admin
        self.event = Event.objects.create(
            name="Test Event",
            description="Test Description",
            start_date="2025-01-01",
            end_date="2025-01-10"
        )
        self.team1 = Team.objects.create(name="Team 1", description="Description 1")
        self.team2 = Team.objects.create(name="Team 2", description="Description 2")
        self.match = Match.objects.create(
            event=self.event,
            team1=self.team1,
            team2=self.team2,
            scheduled_time=now() + timedelta(days=1),
            status="upcoming"
        )
        self.matches_url = reverse('matches')
        self.match_detail_url = reverse('match-detail', kwargs={'pk': self.match.id})


    def test_list_matches(self):
        """
        Test retrieving a list of matches.
        """
        response = self.client.get(self.matches_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['id'], self.match.id)

    def test_create_match(self):
        """
        Test creating a new match.
        """
        data = {
            "event": self.event.id,
            "team1": self.team1.id,
            "team2": self.team2.id,
            "scheduled_time": (now() + timedelta(days=2)).isoformat(),
            "status": "upcoming"
        }
        response = self.client.post(self.matches_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 2)

    def test_retrieve_match(self):
        """
        Test retrieving a single match by ID.
        """
        response = self.client.get(self.match_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.match.id)

    def test_update_match(self):
        """
        Test updating an existing match.
        """
        data = {
            "event": self.event.id,
            "team1": self.team1.id,
            "team2": self.team2.id,
            "scheduled_time": (now() + timedelta(days=3)).isoformat(),
            "status": "completed"
        }
        response = self.client.put(self.match_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.match.refresh_from_db()
        self.assertEqual(self.match.status, "completed")

    def test_delete_match(self):
        """
        Test deleting a match.
        """
        response = self.client.delete(self.match_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Match.objects.count(), 0)
