"""Admin classes for the ad_rotator app."""
from django.contrib import admin

from . import models


class BannerAdAdmin(admin.ModelAdmin):
    """Custom admin for the ``BannerAd`` model."""
    list_display = ('start_date', 'end_date', 'link_url', 'link_alt_text')
    search_fields = ['link_alt_text', 'link_url']


admin.site.register(models.BannerAd, BannerAdAdmin)
