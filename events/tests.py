from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event
from django.contrib.auth import get_user_model

User = get_user_model()


class EventModelTestCase(TestCase):
    """
    Test cases for the Event model.
    """

    def test_default_image_assignment(self):
        """
        Test that the default image is assigned if no image is provided.
        """
        event = Event.objects.create(
            name="Test Event",
            description="Event without image",
            start_date="2025-01-16",
            end_date="2025-01-17",
        )
        self.assertEqual(
            event.image,
            "https://res.cloudinary.com/dzidcvhig/image/upload/v1734180701/gg-ez/defaults/nou2mptttvfkmdtijdhu.webp"
        )

    def test_string_representation(self):
        """
        Test the string representation of the Event model.
        """
        event = Event.objects.create(
            name="Sample Event",
            description="Sample event description",
            start_date="2025-01-16",
            end_date="2025-01-17",
        )
        self.assertEqual(str(event), "Sample Event")


class EventAPITestCase(TestCase):
    """
    Test cases for the Event API.
    """

    def setUp(self):
        self.client = APIClient()
        self.event_url = "/events/"

        # Create and authenticate a staff user
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_create_event(self):
        """
        Test event creation.
        """
        data = {
            "name": "New Event",
            "description": "Description for the new event",
            "start_date": "2025-01-16",
            "end_date": "2025-01-17",
            "image": None,
        }
        response = self.client.post(self.event_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)

    def test_list_events(self):
        """
        Test retrieving a list of events.
        """
        # Clear all events to ensure no leftovers from other tests
        Event.objects.all().delete()

        # Create a single event
        Event.objects.create(
            name="Event 1",
            description="First Event",
            start_date="2025-01-16",
            end_date="2025-01-17"
        )

        # Retrieve the list of events
        response = self.client.get(reverse('event-list'))

        # Assert only one event is returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)

    def test_event_retrieve(self):
        """
        Test retrieving a single event by ID.
        """
        event = Event.objects.create(
            name="Retrieve Test Event",
            description="Testing retrieval",
            start_date="2025-01-16",
            end_date="2025-01-17",
        )
        url = reverse('event-detail', kwargs={'pk': event.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], "Retrieve Test Event")

    def test_update_event(self):
        """
        Test updating an existing event.
        """
        event = Event.objects.create(
            name="Update Test Event",
            description="Old description",
            start_date="2025-01-16",
            end_date="2025-01-17",
        )
        url = reverse(
            'event-detail',
            kwargs={'pk': event.id})  # Use reverse to construct the URL
        data = {
            "name": "Updated Event",
            "description": "Updated description",
            "start_date": "2025-01-16",
            "end_date": "2025-01-18",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        event.refresh_from_db()
        self.assertEqual(event.name, "Updated Event")

    def test_delete_event(self):
        """
        Test deleting an event.
        """
        event = Event.objects.create(
            name="Delete Test Event",
            description="To be deleted",
            start_date="2025-01-16",
            end_date="2025-01-17",
        )
        url = reverse('event-detail', kwargs={'pk': event.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)
