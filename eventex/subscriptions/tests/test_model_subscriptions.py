from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Antonio Thomazinho',
            cpf='12345678901',
            email='apthomazinho@gmail.com',
            phone='21-98020-2530'
        )
        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have on auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)