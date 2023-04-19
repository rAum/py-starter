"""{{ cookiecutter.python_package_name }} version information."""
from pathlib import Path

version_file = Path(__file__).absolute().parents[0] / "VERSION"
__version__ = version_file.read_text(encoding="utf-8").strip()
