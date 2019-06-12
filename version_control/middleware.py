import re

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.deprecation import MiddlewareMixin
from django.utils.encoding import force_text

try:
    import git
    HAS_GITPYTHON = True
except ImportError:
    HAS_GITPYTHON = False

try:
    import hglib
    HAS_HGLIB = True
except ImportError:
    HAS_HGLIB = False


def get_version_control_panel():
    if HAS_GITPYTHON:
        repo = git.Repo(search_parent_directories=True)
        branch = repo.active_branch.name
    elif HAS_HGLIB:
        repo = hglib.open(settings.BASE_DIR)
        branch = repo.branch().decode()
    else:
        return ''

    return render_to_string('version_control_panel.html', {"branch": branch})


class VersionControlMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        content = force_text(response.content, encoding=response.charset)
        insert_before = '</body>'
        pattern = re.escape(insert_before)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        if len(bits) > 1:
            bits[-2] += get_version_control_panel()
            response.content = insert_before.join(bits)
            if response.get("Content-Length", None):
                response["Content-Length"] = len(response.content)

        return response
