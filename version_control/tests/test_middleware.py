from django.test import TestCase
from django.urls import path, reverse
from django.http import HttpResponse
from django.test.utils import override_settings


urlpatterns = [
    path("", lambda request: HttpResponse("<body>OK</body>"), name='index')
]


@override_settings(ROOT_URLCONF="version_control.tests.test_middleware")
class VersionControlMiddlewareTests(TestCase):

    def test_should_add_version_control_bar_to_response(self):
        url = reverse("index")

        response = self.client.get(url)
        response_content = response.content.decode()

        self.assertIn('<div id="version_control_panel">', response_content)
