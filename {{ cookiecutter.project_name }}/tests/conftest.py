"""Pytest configuration for {{cookiecutter.project_name}}."""

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    """Override default location of docker-compose.yml file."""
    # Get the root directory (one level up)
    root_dir = Path(__file__).parent.parent
    return root_dir / "docker-compose.yml"
