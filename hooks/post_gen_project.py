#!/usr/bin/env python
import json
import os
import shutil
from pathlib import Path


use_docker_compose = bool({{cookiecutter.use_docker_compose}})


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not use_docker_compose:
    remove("docker-compose.yml")
    remove("compose")
    remove(".github/workflows/tests_docker.yml")
    remove("tests/test_with_docker_compose_playwright.py")


def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write("\n")


reindent_cookiecutter_json()
