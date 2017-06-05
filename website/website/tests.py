# -*- coding: utf-8 -*-


from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase  
from django.test import TestCase
from django.utils.translation import activate


class DemoTest(TestCase):
    
    def test_demo(self):
        calc =  1 + 1 
        self.assertIs(2, 2)



class HomeNewVisitorTest(LiveServerTestCase): 
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_title(self):
        self.browser.get(self.get_full_url("index"))
        self.assertIn("sogloarcadius", self.browser.title)
	
    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)
    	
    def test_uses_index_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, 'biography/index.html')