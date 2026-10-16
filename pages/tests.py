from django.test import TestCase

from .models import Task


class TaskTests(TestCase):
    def test_new_task_is_open(self):
        task = Task.objects.create(title='Write the CI workflow')
        self.assertFalse(task.done)
        self.assertEqual(str(task), 'Write the CI workflow')


class PageTests(TestCase):
    def test_healthz_answers_ok(self):
        response = self.client.get('/healthz')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'ok')

    def test_status_page_counts_open_tasks(self):
        Task.objects.create(title='Open one')
        Task.objects.create(title='Finished one', done=True)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['open_tasks'], 2)
        self.assertContains(response, 'Open tasks')
