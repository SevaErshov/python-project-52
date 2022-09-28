from django.test import TestCase
from django.test import Client
from statuses.models import Status


class TestStatus(TestCase):
    fixtures = ['fixture_data.json']

    def setUp(self):
        self.client = Client()
        self.username = 'TestUser'
        self.first_name = 'My'
        self.last_name = 'Namer'
        self.password = 'difficultPaSs987'

        self.client.post("/users/create/", data={
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password,
        })
        
        self.client.post('/login/', data={
            'username': self.username,
            'password': self.password,
        })

    def test_create_status_url(self):
        response = self.client.get("/statuses/create/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='statuse_create.html')

    def test_create_form(self):
        response = self.client.post("/statuses/create/", data={
            'name': 'anyname',
        })
        statuses = Status.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(statuses.count(), 6)

    def test_update(self):
        statuses = Status.objects.all()
        success_response = self.client.get('/statuses/8/update/')
        self.client.post('/statuses/8/update/', data={
            'name':'newname',
        })

        self.assertEqual(success_response.status_code, 200)
        self.assertEqual(statuses.get(pk=8).name, 'newname')
        self.assertNotEqual(statuses.get(pk=9).name, 'newname')

    def delete_status(self):
        statuses = Status.objects.all()
        response = self.client.get('/statuses/8/delete/')
        success_response = self.client.post('/statuses/8/delete/')
        error_response = self.client.post('/statuses/12/delete/')

        self.assertEqual(success_response.status_code, 302)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(error_response.status_code, 200)
        self.assertEqual(statuses.count(), 5)