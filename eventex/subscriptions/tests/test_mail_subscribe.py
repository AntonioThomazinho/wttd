from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Antonio Thomazinho', cpf='12345678901',
                    email='apthomazinho@gmail.com', phone='21-98020-2530')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmaçao de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'apthomazinho@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Antonio Thomazinho',
            '12345678901',
            'apthomazinho@gmail.com',
            '21-98020-2530'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)