# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased]

## [2024.5.1]

- Bump requirements

## [2023.10.2]

- Reorganize example project to move manage.py into main directory
- Remove pytest-docker (no longer needed)
- Make Playwright optional
- Make Postgres optional
- Ensure Postgres gets added to settings if selected
- Add option to install only one version of Python
- Ensure coverage.xml file gets written to local directory during workflow
- Add cookiecutter option to specify different repo owner to resolve issue with
  tags when the repo belongs to someone other than the user running cookiecutter (e.g.: an organization)
- Improve docs

## [2023.10.1]

Initial release!

[unreleased]: https://github.com/OmenApps/cookiecutter-django-package/compare/HEAD...HEAD
[2023.10.1]: https://github.com/OmenApps/cookiecutter-django-package/releases/tag/2023.10.1
[2023.10.2]: https://github.com/OmenApps/cookiecutter-django-package/releases/tag/2023.10.2
[2024.5.1]: https://github.com/OmenApps/cookiecutter-django-package/releases/tag/2024.5.1
