[![build status](http://gitlab/kuter/version_control/badges/master/build.svg)](http://gitlab/kuter/version_control/commits/master)
[![coverage report](http://gitlab/kuter/version_control/badges/master/coverage.svg)](http://gitlab/kuter/version_control/commits/master)
=====

Django Version Control
=============================
Third-party app created with https://github.com/kuter/django-plugin-template-cookiecutter

Quick start
-----------
1. Add "version_control" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'version_control',
    ]
2. Enable "version_control" in your settings module as follows::


    MIDDLEWARE = [
        "version_control.middleware.VersionControlMiddleware"
    ]

Old-style middleware::

    MIDDLEWARE_CLASSES = [
        "version_control.middleware.VersionControlMiddleware"
    ]

3. Install third-party modules

For projects running under git source control::

    $ pip install GitPython

For mercurial projects::

    $ pip install hglib
