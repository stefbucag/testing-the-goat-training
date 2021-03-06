from django.http import HttpRequest
from django.urls import resolve
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page
from lists.models import Item, List


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')
