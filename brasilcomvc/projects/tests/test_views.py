from django.contrib.auth import get_user_model
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from brasilcomvc.common.views import LoginRequiredMixin

from ..models import Project
from ..views import ProjectApply

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


class ProjectApplyTestCase(TestCase):

    def setUp(self):
        self.volunteer = User.objects.create_user(
            'volunteer@example.com', '123', full_name='John Doe')
        self.project = Project.objects.create(
            owner=User.objects.create_user('owner@example.com', '123'),
            name='Test Project')
        self.url = reverse(
            'projects:project_apply', kwargs={'slug': self.project.slug})

    def test_inherits_login_required_mixin(self):
        self.assertTrue(issubclass(ProjectApply, LoginRequiredMixin))

    def test_template_used(self):
        self.client.login(username=self.volunteer.email, password='123')
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, 'projects/project_apply.html')
        self.assertContains(resp, self.project.name)

    def test_volunteer_is_able_to_apply(self):
        self.client.login(username=self.volunteer.email, password='123')
        message = 'wat'
        resp = self.client.post(self.url, {'message': message})
        self.assertRedirects(resp, self.project.get_absolute_url())
        self.assertTrue(self.project.applications.exists())

        # Check emails
        emails_sent = {email.to[0]: email for email in mail.outbox}
        self.assertEqual(
            set(emails_sent),
            set([self.volunteer.email, self.project.owner.email]))
        owner_email = emails_sent[self.project.owner.email]
        self.assertIn(self.volunteer.get_short_name(), owner_email.body)
        self.assertIn(message, owner_email.body)
        volunteer_email = emails_sent[self.volunteer.email]
        self.assertIn(self.project.name, volunteer_email.body)

    def test_volunteer_cant_apply_twice(self):
        self.client.login(username=self.volunteer.email, password='123')
        self.project.applications.create(volunteer=self.volunteer, message='')
        resp = self.client.post(self.url, {'message': 'wat'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.project.applications.count(), 1)
        self.assertFalse(mail.outbox)

    def test_owner_cant_apply(self):
        self.client.login(username=self.project.owner.email, password='123')
        resp = self.client.post(self.url, {'message': 'y u so mad'})
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(self.project.applications.exists())
        self.assertFalse(mail.outbox)
