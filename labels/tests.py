from django.test import TestCase
from django.test import Client
from labels.models import Label


class TestLabel(TestCase):
    fixtures = ['new_fixture.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='honeymoon', password='isaliveand')

    def test_create_label_url(self):
        response = self.client.get("/labels/create/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='label_create.html')

    def test_create_form(self):
        response = self.client.post("/labels/create/", data={
            'name': 'anyname',
        })
        labels = Label.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(labels.count(), 4)

    def test_update(self):
        labels = Label.objects.all()
        success_response = self.client.get('/labels/4/update/')
        self.client.post('/labels/4/update/', data={
            'name':'newname',
        })

        self.assertEqual(success_response.status_code, 200)
        self.assertEqual(labels.get(pk=4).name, 'newname')
        self.assertNotEqual(labels.get(pk=2).name, 'newname')

    def delete_label(self):
        labels = Label.objects.all()
        response = self.client.get('/labels/4/delete/')
        success_response = self.client.post('/labels/4/delete/')
        error_response = self.client.post('/labels/3/delete/')

        self.assertEqual(success_response.status_code, 302)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(error_response.status_code, 200)
        self.assertEqual(labels.count(), 3)