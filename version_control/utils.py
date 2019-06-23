from django.utils.module_loading import import_string
from django.conf import settings

from .backends.gitpython import HAS_GITPYTHON, GitPythonBackend
from .backends.mercurial import HAS_HGLIB, HgLibBackend


def get_backend():
    backend_path = getattr(settings, 'VERSION_CONTROL_BACKEND', '')
    try:
        klass = import_string(backend_path)
    except ImportError:
        if HAS_GITPYTHON:
            klass = GitPythonBackend
        elif HAS_HGLIB:
            klass = HgLibBackend
    return klass
