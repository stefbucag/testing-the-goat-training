from django.http import HttpRequest
from django.urls import resolve
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page
from lists.models import Item


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)
