Django Ad Rotator
=================

A reusable Django app for managing and displaying banner ads.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-ad-rotator

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-ad-rotator.git#egg=ad_rotator

Add ``ad_rotator`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'ad_rotator',
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate ad_rotator


Usage
-----

Create banner ads by creating ``BannerAd`` objects in the Django admin.

Hook them up in your tempalte by just adding the ``get_banner`` inclusion tag.

.. code-block:: html

	{% load ad_rotator_tags %}

    {% get_banner %}

Customize how the banner is displayed by overriding the template at
``ad_rotator/partials/banner.html``.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-ad-rotator
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
