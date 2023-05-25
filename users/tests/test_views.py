from django.test import TestCase, Client
from django.urls import reverse, resolve
from users.views import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.signin_url = reverse('signin')
        self.signup_url = reverse('signup')


    def test_signin_get(self):
        response = self.client.get(self.signin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signin.html")

    def test_signup_get(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")

    def test_signin_post(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")


