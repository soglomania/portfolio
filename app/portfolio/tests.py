# -*- coding: utf-8 -*-

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate
from selenium import webdriver


class UiTest(StaticLiveServerTestCase): 

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_en(self):
        activate('en')
        self.selenium.get(self.get_full_url("ui:index"))
        self.assertIn("home", self.selenium.title)

    def test_home_fr(self):
        activate("fr")
        self.selenium.get(self.get_full_url("ui:index"))
        self.assertIn("accueil", self.selenium.title)

    def test_home_es(self):
        activate("es")
        self.selenium.get(self.get_full_url("ui:index"))
        self.assertIn("pagina inicio", self.selenium.title)
        

    def test_search_engines_files(self):
        self.selenium.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.selenium.title)
        self.selenium.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.selenium.title)
