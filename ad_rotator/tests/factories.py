"""Factories for the ad_rotator app."""
from django.utils.timezone import now, timedelta

import factory

from .. import models


class BannerAdFactory(factory.DjangoModelFactory):
    """Factory for the ``BannerAd`` model."""
    FACTORY_FOR = models.BannerAd

    start_date = now() - timedelta(days=7)
    end_date = now() - timedelta(days=7)
    image = factory.django.ImageField()
    link_url = factory.Sequence(lambda n: u'http://example.com/0/'.format(n))
    link_alt_text = factory.Sequence(lambda n: u'link_alt_text {0}'.format(n))
