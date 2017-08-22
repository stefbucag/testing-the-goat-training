from selenium import webdriver
from selenium.webdriver.common import keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # assert 'Django' in browser.title
        # assert 'To-Do' in browser.title, "Browser title was " + browser.title

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').header_text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'

        )

        # She types "Buy peacock feathers" into a test box
        # Edith's hobby is typing a fly-fishing lures
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an items in a to-do list table
        inputbox.send_keys(keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a test box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
