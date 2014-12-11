from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Project

User = get_user_model()


class ProjectListTestCase(TestCase):

    url = reverse('projects:project_list')

    def test_page_opens_successfully(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'projects/project_list.html')


class ProjectDetailsTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            owner=User.objects.create_user('test@example.com', '123'),
            name='Test Project')
        self.url = self.project.get_absolute_url()

    def test_page_opens_successfully(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'projects/project_details.html')
