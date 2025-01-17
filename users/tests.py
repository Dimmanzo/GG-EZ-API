from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class CustomUserModelTestCase(TestCase):
    """
    Tests for the CustomUser model.
    """
    def test_default_user_role(self):
        user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.assertEqual(user.role, "default_user")

    def test_role_assignment(self):
        user = User.objects.create_user(
            username="staffuser",
            password="password123",
            role="staff_user"
        )
        self.assertEqual(user.role, "staff_user")


class CustomRegisterSerializerTestCase(TestCase):
    """
    Tests for the CustomRegisterSerializer.
    """
    def test_validate_successful_registration(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
            'role': 'default_user',
        }
        client = APIClient()
        response = client.post(
            reverse('custom_registration'), data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_password_mismatch(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123',
            'role': 'default_user',
        }
        client = APIClient()
        response = client.post(
            reverse('custom_registration'), data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password2', response.data)

    def test_invalid_email(self):
        data = {
            'username': 'newuser',
            'email': 'invalid-email',
            'password1': 'Password123!',
            'password2': 'Password123!',
            'role': 'default_user',
        }
        client = APIClient()
        response = client.post(
            reverse('custom_registration'), data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)


class UserViewTestCase(TestCase):
    """
    Tests for user views.
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="Password123!",
            role="default_user"
        )

    def test_current_user_role_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('current-user-role'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['role'], self.user.role)
        self.assertEqual(response.data['email'], self.user.email)
