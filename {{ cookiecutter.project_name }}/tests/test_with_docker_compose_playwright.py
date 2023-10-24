"""This is a sample test for Playwright using Docker Compose."""
import logging
import re

import pytest
import requests
from playwright.sync_api import Page
from playwright.sync_api import expect
from requests.exceptions import ConnectionError


def is_responsive(url):
    """Check if a response is returned for a provided url."""
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def http_service(docker_ip, docker_services):
    """Ensure that HTTP service is up and responsive."""
    port = docker_services.port_for("django_test", 8000)
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=lambda: is_responsive(url))

    return url


def test_status_code(http_service):
    """Check the status code of the HTTP service."""
    logging.info(f"http_service: {http_service}")
    response = requests.get(http_service, timeout=60)
    logging.info(f"response: {response}")

    assert response.status_code == 200


def test_has_corrrect_title(http_service, page: Page):
    """Test that the page has the correct title."""
    page.goto(http_service)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("The install worked successfully! Congratulations!"))
