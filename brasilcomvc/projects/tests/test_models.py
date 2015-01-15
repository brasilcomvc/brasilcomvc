# coding: utf8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Project, project_img_upload_to


User = get_user_model()


class ProjectTestCase(TestCase):

    def test_project_slug_gets_generated_correctly(self):
        project = Project(
            owner=User.objects.create_user('test@example.com', '123'),
            name='This is a Test Project')
        project.save()
        self.assertEqual(project.slug, 'this-is-a-test-project')
        old_slug = project.slug
        project.name = 'Some New Name'
        project.save()
        self.assertEqual(project.slug, old_slug)

    def test_project_img_upload_to(self):
        project = Project(slug='wat-is-a-slug')
        filename = 'wat.png'
        expected = 'projects/wat-is-a-slug/img.jpeg'
        self.assertEqual(project_img_upload_to(project, filename), expected)

    def test_auto_geocode_should_fail_with_invalid_address(self):
        project = Project(address='Th1s iz such an 1nv4l1d @ddress')
        self.assertRaises(ValidationError, lambda: project.clean())
        self.assertIsNone(project.latlng)

    def test_auto_geocode_should_work_with_valid_address(self):
        project = Project(address='Sé, São Paulo, Brasil')
        project.clean()
        self.assertIsNotNone(project.latlng)
        # Test approximate geo coordinates
        self.assertEqual(int(project.latlng.x), -23)
        self.assertEqual(int(project.latlng.y), -46)
