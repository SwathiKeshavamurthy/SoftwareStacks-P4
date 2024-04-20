from django.test import TestCase, Client
from django.urls import reverse
from .models import About
from .forms import ContactForm

class AboutMeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_render_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_submit_contact_form_valid_data(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('about'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Submitted Successfully!")

    def test_about_model_data_retrieval(self):
        about = About.objects.create(title='Test About', content='Test content')
        response = self.client.get(reverse('about'))
        self.assertEqual(response.context['about'], about)

    def test_contact_form_initialization(self):
        response = self.client.get(reverse('about'))
        self.assertIsInstance(response.context['contact_form'], ContactForm)

