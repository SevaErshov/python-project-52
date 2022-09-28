from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model


class TestUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.username = 'TestUser'
        self.first_name = 'My'
        self.last_name = 'Namer'
        self.password = 'difficultPaSs987'

    def test_create_page_url(self):
        response = self.client.get("/users/create/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='create_user.html')

    def test_create_form(self):
        response = self.client.post("/users/create/", data={
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password,
        })
        users = get_user_model().objects.all()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(users.count(), 4)


class TestUpdate(TestCase):
    fixtures = ['users.json']

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

        self.users = get_user_model().objects.all()
        new_client = self.users.get(username=self.username)
        self.pk = new_client.id

    def test_update(self):
        response = self.client.get('/users/6/update/')
        success_response = self.client.get('/users/' + str(self.pk) +'/update/')
        self.client.post('/users/' + str(self.pk) +'/update/', data={
            'username': 'MyNewUserName',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(success_response.status_code, 200)
        self.assertEqual(self.users.get(pk=self.pk).username, 'MyNewUserName')
        self.assertNotEqual(self.users.get(pk=self.pk).username, self.username)


class TestDelete(TestCase):
    fixtures = ['users.json']
    
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

        users = get_user_model().objects.all()
        new_client = users.get(username=self.username)
        self.pk = new_client.id

    def test_delete(self):
        response = self.client.get('/users/6/delete/')
        success_response = self.client.post('/users/' + str(self.pk) + '/delete/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(success_response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 3)
