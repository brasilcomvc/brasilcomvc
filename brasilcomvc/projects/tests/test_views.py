from django.test import TestCase

from ..models import Project


class ProjectDetailsTestCase(TestCase):

    fixtures = ('test_users', 'test_projects',)

    def setUp(self):
        self.project = Project.objects.order_by('?')[0]
        self.url = self.project.get_absolute_url()

    def test_page_opens_successfully(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'projects/project_details.html')
