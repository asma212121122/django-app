from django.test import TestCase
from .models import Task

class TaskTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="CI task")
        self.assertEqual(task.title, "CI task")
