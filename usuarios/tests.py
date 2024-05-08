from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User, UserManager

class UserTestCase(TestCase):
    def setUp(self):
        # Set up data for the whole TestCase
        self.user_manager = UserManager()

    def test_create_user(self):
        # Test creating a regular user
        user = self.user_manager.create_user(nombre_usuario='john_doe', email='john@example.com', password='password123')
        self.assertEqual(user.nombre_usuario, 'john_doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        # Test creating a superuser
        superuser = self.user_manager.create_superuser(nombre_usuario='admin', email='admin@example.com', password='admin123')
        self.assertEqual(superuser.nombre_usuario, 'admin')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)

    def test_user_string_representation(self):
        # Test the custom __str__ method
        user = self.user_manager.create_user(nombre_usuario='jane_doe', email='jane@example.com', password='jane123')
        self.assertEqual(str(user), 'jane_doe')

    def test_user_with_no_username(self):
        # Test that ValueError is raised when no username is provided
        with self.assertRaises(ValueError):
            self.user_manager.create_user(nombre_usuario='', email='user@example.com', password='test123')

    def test_user_with_no_email(self):
        # Test that ValueError is raised when no email is provided
        with self.assertRaises(ValueError):
            self.user_manager.create_user(nombre_usuario='user_without_email', email='', password='test123')

