"""Models for the ad_rotator app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BannerAd(models.Model):
    """
    Holds the content of the ad.

    :start_date: The first date, the ad will be displayed.
    :end_date: The last date, the ad will be displayed.
    :image: The banner ad's image.
    :link_url: The url of the banner link.
    :link_alt_text: The links alt attribute text.

    """
    start_date = models.DateField(
        verbose_name=_('Start date'),
    )

    end_date = models.DateField(
        verbose_name=_('End date'),
    )

    image = models.ImageField(
        upload_to='banner_ads',
        verbose_name=_('Image'),
    )

    link_url = models.URLField(
        verbose_name=_('Link URL'),
        max_length=256,
    )

    link_alt_text = models.CharField(
        verbose_name=_('Link alt text'),
        max_length=64,
    )

    def __unicode__(self):
        return self.link_alt_text

    class Meta:
        ordering = ('start_date', )
