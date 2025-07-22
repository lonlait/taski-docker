from django.test import Client, TestCase
from . import models


class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_exists(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_task_creation(self):
        data = {'title': 'Sample Task', 'description': 'This is a sample task for testing'}
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(models.Task.objects.filter(title='Sample Task').exists())
