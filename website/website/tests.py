# -*- coding: utf-8 -*-


from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase  
from django.test import TestCase
from django.utils.translation import activate

# Test homepage

class HomeTest(LiveServerTestCase): 
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_title(self):
        activate('fr')
        self.browser.get(self.get_full_url("index"))
        self.assertIn("sogloarcadius", self.browser.title)
	
    # make sure that robot and human file accessible 
    #due to language support django add locale code in url, 
    # ( http://domain.com/robot.txt & http://domain.com/human.txt)

    def test_search_engines_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)
    	
    def test_uses_index_template(self):
        activate('fr')
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, 'home/index.html')