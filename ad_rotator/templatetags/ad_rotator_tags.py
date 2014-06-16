"""Template tags for the ``ad_rotator`` app."""
import random

from django import template
from django.utils.timezone import now

from .. import models

register = template.Library()


@register.inclusion_tag('ad_rotator/partials/banner.html')
def get_banner():
    """Returns a random ``BannerAd`` instance."""
    banner = None

    banners = models.BannerAd.objects.filter(
        start_date__lte=now().date(), end_date__gte=now().date())

    if banners.count():
        banner = random.choice(banners)

    return {'banner': banner}
