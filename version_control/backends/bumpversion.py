try:
    import tomllib
except ImportError:
    import tomli as tomllib

from version_control.backends.base import BaseVersionControl


class BumpversionVersionControlBackend(BaseVersionControl):
    @classmethod
    def get_current_branch_name(self):
        with open("pyproject.toml", "rb") as file:
            pyproject = tomllib.load(file)

        # Access the version from the tool.bumpversion section
        current_version = pyproject["tool"]["bumpversion"]["current_version"]

        return f"{current_version}"
