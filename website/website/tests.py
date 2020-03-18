# -*- coding: utf-8 -*-


from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase  
from django.test import TestCase
from django.utils.translation import activate


class RootApiTest(StaticLiveServerTestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_api_root_en(self):
        activate('en')
        self.browser.get(self.get_full_url("api-me"))
        self.assertIn("Personal Info Api", self.browser.title)

    def test_api_root_fr(self):
        activate("fr")
        self.browser.get(self.get_full_url("api-me"))
        self.assertIn("Personal Info Api", self.browser.title)

    def test_api_root_es(self):
        activate("es")
        self.browser.get(self.get_full_url("api-me"))
        self.assertIn("Personal Info Api", self.browser.title)
        

    def test_search_engines_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)


    
