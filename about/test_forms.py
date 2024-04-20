from django.test import TestCase
from .forms import ContactForm
from .models import ContactRequest

class ContactFormTestCase(TestCase):
    def test_contact_form_valid_data(self):
        """Test the ContactForm with valid input data."""
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid_data(self):
        """Test the ContactForm with invalid input data."""
        data = {
            'name': '',  # Empty name should be invalid
            'email': 'john.doe@example.com',
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_contact_form_invalid_email(self):
        """Test the ContactForm with an invalid email."""
        data = {
            'name': 'John Doe',
            'email': 'not-an-email',  # Invalid email
            'message': 'Hello, this is a test message.'
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_contact_form_empty_message(self):
        """Test the ContactForm with an empty message."""
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': ''  # Empty message should be invalid
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)
