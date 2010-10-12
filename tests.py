from django.test import TestCase
from bb_dataset.models import *
from django.contrib.auth.models import *
from django.db import IntegrityError
from django.test.client import Client

class BBDatasetTestCase(TestCase):
    fixtures = ['bb_dataset', ]


    def testFixtureLoading(self):
        self.assertEquals(1, Race.objects.all().count())
        human = Race.objects.get(slug='human')
        self.assertEquals('Human', human.name)

    def testApiReturnsListOfRaces(self):
        c = Client()
        response = c.get('/dataset/race/human/')
        self.assertContains(response, '"name": "Human"')

    def testApiReturnsSpecificRaceData(self):
        c = Client()
        response = c.get('/dataset/race/human/')
        self.assertContains(response, '"name": "Human"') 
