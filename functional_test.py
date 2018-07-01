from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit

    def test_can_start(self):

        # Ploy find web quiz in url localhost port 8000
        self.browser.get('http://localhost:8000')

        # Ploy see title name Quiz in web
        self.assertIn('Quiz', self.browser.title)

        # Ploy see question in web
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('1 + 1 = 3 ?', header_text)

        # Ploy select choice from question
        # Ploy select choice number 1 is True
        choice = self.browser.find_element_by_id('1')
        choice.click()
        time.sleep(1)

        # When Ploy click choice
        # Web app show vote answer
        self.browser.get('http://localhost:8000/vote')
        # Ploy click back for vote again
        back = self.browser.find_element_by_id('id_back')
        back.click()
        time.sleep(1)

        self.fail('Finish the test!')




if __name__ == '__main__':
    unittest.main(warnings='ignore')
