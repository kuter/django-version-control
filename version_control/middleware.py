import re

from django.template.loader import render_to_string
from django.utils.encoding import force_text

from .backends.gitpython import GitPythonBackend
from .backends.mercurial import HgLibBackend

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


def get_version_control_panel():
    if GitPythonBackend.get_current_branch_name():
        branch = GitPythonBackend.get_current_branch_name()
    elif HgLibBackend.get_current_branch_name():
        branch = HgLibBackend.get_current_branch_name()
    else:
        branch = ""

    return render_to_string("version_control_panel.html", {"branch": branch})


class VersionControlMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        encoding = response.charset if hasattr(response, "charset") else "utf-8"
        content = force_text(response.content, encoding=encoding)
        insert_before = "</body>"
        pattern = re.escape(insert_before)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        if len(bits) > 1:
            bits[-2] += get_version_control_panel()
            response.content = insert_before.join(bits)
            if response.get("Content-Length", None):
                response["Content-Length"] = len(response.content)

        return response
