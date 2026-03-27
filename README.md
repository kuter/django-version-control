[![License](https://img.shields.io/pypi/l/version_control.svg)](https://raw.githubusercontent.com/kuter/django-version-control/master/LICENSE)
[![Latest PyPI version](https://img.shields.io/pypi/v/version_control.svg)](https://pypi.python.org/pypi/version_control/)
[![Build Status](https://travis-ci.org/kuter/django-version-control.svg?branch=master)](https://travis-ci.org/kuter/django-version-control)
[![Coverage Status](https://coveralls.io/repos/github/kuter/django-version-control/badge.svg?branch=master)](https://coveralls.io/github/kuter/django-version-control?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

# Django Version Control

A third-party Django application generated with [django-plugin-template-cookiecutter](https://github.com/kuter/django-plugin-template-cookiecutter).

## Quick Start

### 1. Installation

Install the package via pip:

```bash
pip install version_control
```

### 2. Configuration

Add `"version_control"` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # ...existing apps...
    "version_control",
]
```

Enable the middleware by adding it to your `MIDDLEWARE` setting:

```python
MIDDLEWARE = [
    # ...existing middleware...
    "version_control.middleware.VersionControlMiddleware",
]
```

### 3. Version Control Dependencies

Depending on the version control system used by your project, install the corresponding third-party modules:

**For Git projects:**

```bash
pip install GitPython
```

**For Mercurial projects:**

```bash
pip install hglib         # Python 3.x
pip install python-hglib  # Python 2.7.x
```

**For projects with bumpversion:**

```bash
pip install bumpversion
```

## Supported Backends

You can explicitly set which backend to use by defining `VERSION_CONTROL_BACKEND` in your `settings.py`. The available backends are:

### Git
Requires the `GitPython` dependency.
```python
VERSION_CONTROL_BACKEND = "version_control.backends.git.GitBackend"
```

### Mercurial
Requires the `hglib` (or `python-hglib`) dependency.
```python
VERSION_CONTROL_BACKEND = "version_control.backends.mercurial.MercurialBackend"
```

### Bumpversion
Reads the version directly from your bumpversion configuration.
```python
VERSION_CONTROL_BACKEND = "version_control.bumpversion.BumpversionVersionControlBackend"
```

### Dummy
A basic backend useful for testing or local development environments that lack a version control system.
```python
VERSION_CONTROL_BACKEND = "version_control.dummy.DummyBackend"
```

