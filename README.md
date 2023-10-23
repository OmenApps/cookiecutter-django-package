# cookiecutter-django-package

<!-- badges-begin -->

[![Status][status badge]][status badge]
[![Python Version][python version badge]][github page]
[![CalVer][calver badge]][calver]
[![License][license badge]][license]<br>
[![Read the documentation][readthedocs badge]][readthedocs page]
[![Tests][github actions badge]][github actions page]
[![Codecov][codecov badge]][codecov page]<br>
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Black codestyle][black badge]][black project]
[![Contributor Covenant][contributor covenant badge]][code of conduct]

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black project]: https://github.com/psf/black
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.RR-22bfda.svg
[calver]: http://calver.org/
[code of conduct]: https://github.com/omenapps/cookiecutter-django-package/blob/main/CODE_OF_CONDUCT.md
[codecov badge]: https://codecov.io/gh/omenapps/cookiecutter-django-package-instance/branch/main/graph/badge.svg
[codecov page]: https://codecov.io/gh/omenapps/cookiecutter-django-package-instance
[contributor covenant badge]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[github actions badge]: https://github.com/omenapps/cookiecutter-django-package/workflows/Tests/badge.svg
[github actions page]: https://github.com/omenapps/cookiecutter-django-package/actions?workflow=Tests
[github page]: https://github.com/omenapps/cookiecutter-django-package
[license badge]: https://img.shields.io/github/license/omenapps/cookiecutter-django-package
[license]: https://opensource.org/licenses/MIT
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/pypi/pyversions/cookiecutter-django-package-instance
[readthedocs badge]: https://img.shields.io/readthedocs/cookiecutter-django-package/latest.svg?label=Read%20the%20Docs
[readthedocs page]: https://cookiecutter-django-package.readthedocs.io/
[status badge]: https://badgen.net/badge/status/alpha/d8624d

<!-- badges-end -->

[Cookiecutter] template for a Django package adapted from
[Hypermodern Python Cookiecutter] from [Claudio Jolowicz].

✨📚✨ [Read the full documentation][readthedocs page]

[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python cookiecutter]: https://github.com/omenapps/cookiecutter-django-package/
[Claudio Jolowicz]: https://github.com/cjolowicz/

## Usage

```console
cookiecutter gh:OmenApps/cookiecutter-django-package --checkout=2023.10.1
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [Poetry]
- Test automation with [Nox]
- Linting with [pre-commit] and [Flake8]
- Continuous integration with [GitHub Actions]
- Documentation with [Sphinx], [MyST], and [Read the Docs] using the [furo] theme
- Automated uploads to [PyPI] and [TestPyPI]
- Automated release notes with [Release Drafter]
- Automated dependency updates with [Dependabot]
- Code formatting with [Black] and [Prettier]
- Import sorting with [isort]
- Testing with [pytest] and [pytest-django]
- Optional testing with Docker Compose (using [pytest-docker]) and [PlayWright]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]
- Command-line interface with [Click]
- Automated Python syntax upgrades with [pyupgrade]
- Security audit with [Bandit] and [Safety]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc] and [napoleon]
- Generate command-line reference with [sphinx-click]
- Manage project labels with [GitHub Labeler]
- Run an instance of Postgresql and the example project (with your django package installed locally) with [Docker Compose]

The template supports Python 3.9, 3.10, 3.11, and 3.12.

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[black]: https://github.com/psf/black
[click]: https://click.palletsprojects.com/
[codecov]: https://about.codecov.io/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[docker compose]: https://docs.docker.com/compose/
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[isort]: https://pycqa.github.io/isort/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[playwright]: https://playwright.dev/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[pytest-django]: https://pytest-django.readthedocs.io/en/latest/
[pytest-docker]: https://github.com/avast/pytest-docker/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[safety]: https://github.com/pyupio/safety
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
[xdoctest]: https://github.com/Erotemic/xdoctest

<!-- features-end -->
