import os.path
import shutil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File

from ..models import Project


User = get_user_model()


class ProjectTestMixin(object):
    '''
    Ease the Project creation process, given the need to save/delete
    an image to the instance.
    '''

    def setUp(self):
        self.project = Project.objects.create(
            owner=User.objects.create_user('owner@example.com', '123'),
            name='Test Project')

        # Save Project img
        img_path = os.path.join(os.path.dirname(__file__), 'empty_img.png')
        self.project.img.save(
            os.path.basename(img_path), File(open(img_path, 'rb')))
        self.project.save()

    def tearDown(self):
        # Drop the Project img and its generated thumbnails
        shutil.rmtree(os.path.join(
            settings.MEDIA_ROOT, os.path.dirname(self.project.img.name)))
