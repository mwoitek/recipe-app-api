"""
Tests for the Django admin modifications.
"""

from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.admin_user = (
            get_user_model().objects.create_superuser(  # pyright: ignore
                email="admin@example.com",
                password="testpass123",
            )
        )
        self.client = Client()
        self.client.force_login(user=self.admin_user)
        self.user = get_user_model().objects.create_user(  # pyright: ignore
            email="user@example.com",
            password="testpass123",
            name="Test User",
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)
