from django.test import TestCase,SimpleTestCase
from django.urls import reverse # import reverse method

# Create your tests here.

class SnacksTest(SimpleTestCase):
    def test_home_page_status_code(self):
        expected=200
        url = reverse('home')
        responce=self.client.get(url)
        actual = responce.status_code
        #assert actual=expected
        self.assertAlmostEquals(expected,actual)

    def test_about_page_status_code(self):
        expected=200
        url=reverse('about')
        responce=self.client.get(url)
        actual=responce.status_code
        self.assertEquals(expected,actual)

    def test_home_page_template(self):
        url = reverse('home')
        responce=self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(responce,actual)

    def test_about_page_template(self):
        url=reverse('about')
        responce=self.client.get(url)
        actual='about.html'
        self.assertTemplateUsed(responce,actual)