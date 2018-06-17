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
        self.browser.get('http://localhost:8000')
        self.assertIn('Quiz', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('1 + 1 = 3 ?', header_text)

        choice = self.browser.find_element_by_id('1')
        choice.click()
        time.sleep(1)

        back = self.browser.find_element_by_id('id_back')
        back.click()
        time.sleep(1)

        self.fail('Finish the test!')




if __name__ == '__main__':
    unittest.main(warnings='ignore')
