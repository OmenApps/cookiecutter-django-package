# Cookiecutter Django Package

```{toctree}
---
hidden: true
maxdepth: 1
---

Quickstart <quickstart>
guide
contributing
Code of Conduct <codeofconduct>
license
Changelog <https://github.com/omenapps/cookiecutter-django-package/releases>
```

```{include} ../README.md
---
start-after: <!-- badges-begin -->
end-before: <!-- badges-end -->
---
```

[Cookiecutter] template for a Django package based on the
[Hypermodern Python Cookiecutter], and adapted for developing Django packages

## Usage

```console
$ cookiecutter gh:omenapps/cookiecutter-django-package --checkout="2023.10.1"
```

## Features

```{include} ../README.md
---
start-after: <!-- features-begin -->
end-before: <!-- features-end -->
---
```

## FAQ

### What is this project about?

The mission of this project is to enable current best practices
through modern Python and Django tooling.

### What makes this project different from other Django package templates?

This is a general-purpose template for Django packages.

Our goals are:

- Focus on simplicity
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- [Poetry][1] for packaging and dependency management
- [Nox][2] for automation of checks and other development tasks
- [GitHub Actions][3] for continuous integration and delivery

[1]: https://python-poetry.org/
[2]: https://nox.thea.codes/
[3]: https://github.com/features/actions

[cookiecutter]: https://github.com/audreyr/cookiecutter
[Cookiecutter Django Package]: https://github.com/omenapps/cookiecutter-django-package
[Hypermodern Python Cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
