from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Project

User = get_user_model()


class ProjectTestCase(TestCase):

    def test_project_slug_gets_generated_correctly(self):
        project = Project(
            owner=User.objects.create_user('test@example.com', '123'),
            name='This is a Test Project',
        )
        project.save()
        self.assertEqual(project.slug, 'this-is-a-test-project')
        old_slug = project.slug
        project.name = 'Some New Name'
        project.save()
        self.assertEqual(project.slug, old_slug)
