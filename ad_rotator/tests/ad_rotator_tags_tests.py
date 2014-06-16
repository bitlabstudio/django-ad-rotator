"""Tests for the template tags of the ``ad_rotator`` app."""
from django.test import TestCase

from . import factories
from ..templatetags import ad_rotator_tags


class GetBannerTestCase(TestCase):
    """Tests for the ``get_banner`` tempalte tag."""
    longMessage = True

    def setUp(self):
        self.banners = factories.BannerAdFactory.create_batch(4)

    def test_tag(self):
        self.assertIn(ad_rotator_tags.get_banner()['banner'], self.banners,
                      msg=('The tag should return a random banner.'))

        for banner in self.banners:
            banner.delete()

        self.assertIsNone(ad_rotator_tags.get_banner()['banner'], msg=(
                          'There should be no banner returned.'))
