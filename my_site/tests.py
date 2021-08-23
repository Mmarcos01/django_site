# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class ThingsTests(SimpleTestCase):
    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_poetry_status_code(self):
        url = reverse('poetry')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_poetry_template(self):
        url = reverse('poetry')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'poetry.html')
        self.assertTemplateUsed(response, 'base.html')
