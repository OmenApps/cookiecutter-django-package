#!/usr/bin/env python
import json
import os
import shutil
from pathlib import Path

use_playwright = bool("{{cookiecutter.use_playwright}}" == "y")


def remove(filepath):
    """Remove file or directory."""
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if not use_playwright:
    # Remove the playwright-specific files.
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
