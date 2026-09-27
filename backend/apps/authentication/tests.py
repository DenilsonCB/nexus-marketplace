from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTests(TestCase):
    """Test suite for the custom User model."""

    def test_create_customer_user(self):
        """A standard user should default to customer role."""
        # Arrange & Act
        user = User.objects.create_user(
            email='customer@example.com',
            username='customer_test',
            password='testpasword123'
        )

        # Asert
        self.assertEqual(user.email, 'customer@example.com')
        self.assertTrue(user.is_customer)
        self.assertFalse(user.is_merchant)
        self.assertFalse(user.is_staff)

    def test_create_merchant_user(self):
        """A user created with merchant flag should respect these flags."""
        # Arrange & Act
        user = User.objects.create_user(
            email='merchant@example.com',
            username='merchant_test',
            password='testpassword123',
            is_merchant=True,
            is_customer=False
        )

        # Assert
        self.assertEqual(user.email, 'merchant@example.com')
        self.assertTrue(user.is_merchant)
        self.assertFalse(user.is_customer)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Superuser creation should automatically set admin flags."""
        # Arrange & Act
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            username='admin_test',
            password='superpassword123'
        )

        # Assert
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)