from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from teams.models import Team, Player

User = get_user_model()


class TeamModelTestCase(TestCase):
    """
    Test cases for the Team model.
    """

    def test_team_creation_with_default_logo(self):
        """
        Test creating a team without a logo assigns the default logo.
        """
        team = Team.objects.create(
            name="Test Team",
            description="A valid description"
        )
        self.assertEqual(
            team.logo,
            "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180783/gg-ez/defaults/xgtwsoqklrrtgyeqcgq0.webp"
        )

    def test_team_invalid_name(self):
        """
        Test that creating a team with a blank name raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            team = Team(name="   ", description="A valid description")
            team.full_clean()

    def test_team_invalid_description(self):
        """
        Test that a description shorter than 10 chars raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            team = Team(name="Valid Name", description="Short")
            team.full_clean()


class PlayerModelTestCase(TestCase):
    """
    Test cases for the Player model.
    """

    def test_player_creation_with_default_avatar(self):
        """
        Test creating a player without an avatar assigns the default avatar.
        """
        player = Player.objects.create(name="Test Player", role="Support")
        self.assertEqual(
            player.avatar,
            "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180756/gg-ez/defaults/vlhxug3hav82zlm6thbf.webp"
        )

    def test_player_invalid_name(self):
        """
        Test that creating a player with a blank name raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            player = Player(name="   ", role="Support")
            player.full_clean()

    def test_player_invalid_role(self):
        """
        Test that creating a player with a blank role raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            player = Player(name="Valid Name", role="   ")
            player.full_clean()


class TeamsAPITestCase(TestCase):
    """
    Test cases for Teams API.
    """

    def setUp(self):
        Team.objects.all().delete()
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        self.client.force_authenticate(user=self.admin_user)
        Team.objects.all().delete()
        self.team_url = '/teams/'

    def test_create_team(self):
        data = {
            "name": "Team 1",
            "description": "A strong team."
        }
        response = self.client.post(self.team_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)

    def test_list_teams(self):
        """
        Test retrieving a list of teams.
        """
        Team.objects.create(
            name="Team 1",
            description="First Team Description"
        )
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.data['count'], 1)


class PlayersAPITestCase(TestCase):
    """
    Test cases for Players API.
    """

    def setUp(self):
        Player.objects.all().delete()
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        self.client.force_authenticate(user=self.admin_user)
        Player.objects.all().delete()
        self.team = Team.objects.create(
            name="Team 1",
            description="A strong team."
        )
        self.player_url = '/players/'

    def test_create_player(self):
        data = {
            "name": "Player 1",
            "role": "Support",
            "team": self.team.id
        }
        response = self.client.post(self.player_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 1)

    def test_list_players(self):
        """
        Test retrieving a list of players.
        """
        Player.objects.create(name="Player 1", role="Support", team=self.team)
        response = self.client.get(reverse('player-list'))
        self.assertEqual(response.data['count'], 1)
