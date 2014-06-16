"""Tests for the models of the ad_rotator app."""
from django.test import TestCase

from . import factories


class BannerAdTestCase(TestCase):
    """Tests for the ``BannerAd`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``BannerAd`` model."""
        bannerad = factories.BannerAdFactory()
        self.assertTrue(bannerad.pk)
