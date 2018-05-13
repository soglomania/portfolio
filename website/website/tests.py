# -*- coding: utf-8 -*-


from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase  
from django.test import TestCase
from django.utils.translation import activate


class HomeAppTest(StaticLiveServerTestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_title_en(self):
        activate('en')
        self.browser.get(self.get_full_url("home-index"))
        self.assertIn("About", self.browser.title)

    def test_home_title_fr(self):
        activate("fr")
        self.browser.get(self.get_full_url("home-index"))
        self.assertIn("A propos", self.browser.title)

    def test_home_title_es(self):
        activate("es")
        self.browser.get(self.get_full_url("home-index"))
        self.assertIn("Biografia", self.browser.title)
        
    def test_uses_index_template(self):
        response = self.client.get(reverse("home-index"))
        self.assertTemplateUsed(response, "home/base.html")
        self.assertTemplateUsed(response, 'home/index.html')

    def test_search_engines_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)


class PortfolioAppTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
    
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
    
    def test_navigate_to_portfolio_en(self):
        activate("en")
        self.browser.get(self.get_full_url("project-list"))
        self.assertIn("Projects", self.browser.title)
    
    def test_navigate_to_portfolio_fr(self):
        activate("fr")
        self.browser.get(self.get_full_url("project-list"))
        self.assertIn("Projets", self.browser.title)

    def test_navigate_to_portfolio_es(self):
        activate("es")
        self.browser.get(self.get_full_url("project-list"))
        self.assertIn("Proyectos", self.browser.title)

    def test_uses_portolio_template(self):
        response = self.client.get(reverse("project-list"))
        self.assertTemplateUsed(response, "home/base.html")
        self.assertTemplateUsed(response, "portfolio/project_list.html")

    
