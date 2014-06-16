Django Ad Rotator
============

A reusable Django app for managing and displaying banner ads.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-ad-rotator

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-ad-rotator.git#egg=ad_rotator

TODO: Describe further installation steps (edit / remove the examples below):

Add ``ad_rotator`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'ad_rotator',
    )

Add the ``ad_rotator`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^ad-rotator/', include('ad_rotator.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load ad_rotator_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate ad_rotator


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


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
