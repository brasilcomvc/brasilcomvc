from django.test import TestCase

from ..models import Project


class ProjectTestCase(TestCase):

    def test_project_slug_gets_generated_correctly(self):
        project = Project(name='This is a Test Project')
        project.clean()
        self.assertEqual(project.slug, 'this-is-a-test-project')
