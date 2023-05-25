from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

    def test_list_url_is_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_list_url_is_resolved(self):
        url = reverse('reg_face')
        self.assertEquals(resolve(url).func, reg_face)

    def test_list_url_is_resolved(self):
        url = reverse('reg_face/register_captured_face')
        self.assertEquals(resolve(url).func, register_captured_face)

    def test_list_url_is_resolved(self):
        url = reverse('signout')
        self.assertEquals(resolve(url).func, signout)