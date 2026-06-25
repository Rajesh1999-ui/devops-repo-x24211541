"""Tests for accounts app."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from shop.models import Product, Category

User = get_user_model()


class UserModelTest(TestCase):
    """Test cases for User model."""

    def setUp(self):
        """Set up test data."""
        self.user_data = {
            'email': 'test@example.com',
            'full_name': 'Test User',
            'password': 'testpass123'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_user(self):
        """Test creating a regular user."""
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.full_name, 'Test User')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_admin)
        self.assertFalse(self.user.is_manager)
        self.assertTrue(self.user.check_password('testpass123'))

    def test_create_user_without_email(self):
        """Test creating user without email raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            User.objects.create_user(
                email=None,
                full_name='Test User',
                password='testpass123'
            )
        self.assertEqual(str(cm.exception), 'Email is required!')

    def test_create_user_without_full_name(self):
        """Test creating user without full_name raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            User.objects.create_user(
                email='test@example.com',
                full_name=None,
                password='testpass123'
            )
        self.assertEqual(str(cm.exception), 'full name is required!')

    def test_create_superuser(self):
        """Test creating a superuser."""
        superuser = User.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            password='adminpass123'
        )
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)

    def test_user_str_method(self):
        """Test the __str__ method of User model."""
        self.assertEqual(str(self.user), 'test@example.com')

    def test_user_has_perm(self):
        """Test has_perm method."""
        self.assertTrue(self.user.has_perm(None))

    def test_user_has_module_perms(self):
        """Test has_module_perms method."""
        self.assertTrue(self.user.has_module_perms(None))

    def test_is_staff_property(self):
        """Test is_staff property."""
        self.assertFalse(self.user.is_staff)
        admin_user = User.objects.create_superuser(
            email='admin2@example.com',
            full_name='Admin User 2',
            password='adminpass123'
        )
        self.assertTrue(admin_user.is_staff)

    def test_user_likes_count(self):
        """Test get_likes_count method."""
        # Create a category (use correct field names)
        category = Category.objects.create(
            title='Test Category',  # Assuming 'title' instead of 'name'
            slug='test-category'
        )
        
        # Create products
        product1 = Product.objects.create(
            title='Product 1',
            slug='product-1',
            price=100,
            category=category
        )
        product2 = Product.objects.create(
            title='Product 2',
            slug='product-2',
            price=200,
            category=category
        )
        
        # Initially likes count should be 0
        self.assertEqual(self.user.get_likes_count(), 0)
        
        # Add likes
        self.user.likes.add(product1)
        self.assertEqual(self.user.get_likes_count(), 1)
        
        self.user.likes.add(product2)
        self.assertEqual(self.user.get_likes_count(), 2)

    def test_user_email_uniqueness(self):
        """Test that email must be unique."""
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email='test@example.com',  # Same email as existing
                full_name='Another User',
                password='anotherpass'
            )


class UserManagerTest(TestCase):
    """Test cases for UserManager."""

    def test_create_user(self):
        """Test create_user method of UserManager."""
        user = User.objects.create_user(
            email='manager_test@example.com',
            full_name='Manager Test',
            password='testpass123'
        )
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'manager_test@example.com')
        self.assertTrue(user.check_password('testpass123'))

    def test_create_superuser(self):
        """Test create_superuser method of UserManager."""
        superuser = User.objects.create_superuser(
            email='super@example.com',
            full_name='Super User',
            password='superpass123'
        )
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_staff)

    def test_create_user_without_email_raises_error(self):
        """Test creating user without email raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            User.objects.create_user(
                email='',
                full_name='Test',
                password='testpass'
            )
        self.assertEqual(str(cm.exception), 'Email is required!')

    def test_create_superuser_without_is_admin(self):
        """Test creating superuser sets is_admin to True."""
        superuser = User.objects.create_superuser(
            email='super2@example.com',
            full_name='Super User 2',
            password='superpass123'
        )
        self.assertTrue(superuser.is_admin)


class UserModelFieldTest(TestCase):
    """Test cases for User model fields."""

    def test_email_field_max_length(self):
        """Test email field max length."""
        email_field = User._meta.get_field('email')
        self.assertEqual(email_field.max_length, 100)
        self.assertTrue(email_field.unique)

    def test_full_name_field_max_length(self):
        """Test full_name field max length."""
        full_name_field = User._meta.get_field('full_name')
        self.assertEqual(full_name_field.max_length, 100)

    def test_boolean_fields_default_values(self):
        """Test boolean fields default values."""
        user = User.objects.create_user(
            email='defaults@example.com',
            full_name='Defaults Test',
            password='testpass123'
        )
        self.assertFalse(user.is_admin)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_manager)

    def test_username_field(self):
        """Test USERNAME_FIELD is set to email."""
        self.assertEqual(User.USERNAME_FIELD, 'email')

    def test_required_fields(self):
        """Test REQUIRED_FIELDS contains full_name."""
        self.assertIn('full_name', User.REQUIRED_FIELDS)
        