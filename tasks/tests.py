from django.test import TestCase
from django.test import Client
from tasks.models import Task
from statuses.models import Status
from django.contrib.auth.models import User


class TestTask(TestCase):
    fixtures = ['new_fixture.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='honeymoon', password='isaliveand')

    def test_create_status_url(self):
        response = self.client.get("/tasks/create/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='task_create.html')

    def test_create_form(self):
        response = self.client.post("/tasks/create/", data={
            'name': 'anyname',
            'description': 'anydesc',
            'status': 12,
            'executor': 9,
            'labels': 2,
        })
        tasks = Task.objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(tasks.count(), 5)

    def test_update(self):
        tasks = Task.objects.all()
        success_response = self.client.get('/tasks/3/update/')
        self.client.post('/tasks/3/update/', data={
            'name': 'newname',
            'description': 'anydesc',
            'status': 12,
            'executor': 9,
            'labels': 3
        })

        self.assertEqual(success_response.status_code, 200)
        self.assertEqual(tasks.get(pk=3).name, 'newname')
        self.assertNotEqual(tasks.get(pk=4).name, 'newname')

    def delete_status(self):
        tasks = Task.objects.all()
        response = self.client.get('/tasks/3/delete/')
        success_response = self.client.post('/tasks/3/delete/')

        self.assertEqual(success_response.status_code, 302)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(tasks.count(), 4)