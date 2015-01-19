from django.test import TestCase

from ..models import (
    HomeBanner,
    homebanner_image_upload_to,
    homebanner_video_upload_to,)


class HomeBannerTestCase(TestCase):

    def test_image_upload_to(self):
        banner = HomeBanner.objects.create()
        self.assertEqual(
            homebanner_image_upload_to(banner, 'whatever.png'),
            'homebanners/{:%Y-%m-%d}/image.jpeg'.format(banner.created))

    def test_video_upload_to(self):
        banner = HomeBanner.objects.create()
        self.assertEqual(
            homebanner_video_upload_to(banner, 'whatever.webm'),
            'homebanners/{:%Y-%m-%d}/video.webm'.format(banner.created))
