{% if cookiecutter.use_playwright == "y" %}FROM mcr.microsoft.com/playwright:v1.44.0-jammy{% else %}FROM ubuntu:24.04{% endif %}

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app
ARG DEBIAN_FRONTEND=noninteractive
ARG MULTIPLE_PYTHON  # Set to True if you want to use multiple Python versions

ARG PYTHON_3_9=3.9.19
ARG PYTHON_3_10=3.10.14
ARG PYTHON_3_11=3.11.9
ARG PYTHON_3_12=3.12.3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COMPOSE_DOCKER_CLI_BUILD 1
ENV DOCKER_BUILDKIT 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install apt packages
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update \
    && apt-get --no-install-recommends install -y \
    # Some basic tools and libraries
    bash curl wget git make \
    build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev{% if cookiecutter.use_postgres == "y" %} \
    # psycopg2 dependencies
    libpq-dev{% endif %}

# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT ${APP_HOME}/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Install Python version(s)
RUN if [ "$MULTIPLE_PYTHON" = "True" ] ; then \
    pyenv install ${PYTHON_3_12}; \
    pyenv install ${PYTHON_3_11}; \
    pyenv install ${PYTHON_3_10}; \
    pyenv install ${PYTHON_3_9}; \
    else \
    pyenv install {{ cookiecutter.docker_compose_python_version }}; \
    fi

# Initialize pyenv
RUN eval "$(pyenv init -)"

# Add deadsnakes PPA
RUN apt-get install -y software-properties-common
RUN add-apt-repository 'ppa:deadsnakes/ppa'
RUN apt-get update

# Make Python version(s) accessible in the project and install Python venv
RUN if [ "$MULTIPLE_PYTHON" = "True" ] ; then \
    apt-get install -y python3.12-venv python3.9-venv python3.10-venv python3.11-venv; \
    pyenv local ${PYTHON_3_12} ${PYTHON_3_9} ${PYTHON_3_10} ${PYTHON_3_11}; \
    else \
    apt-get install -y python{{ cookiecutter.docker_compose_python_version }}-venv; \
    pyenv local {{ cookiecutter.docker_compose_python_version }}; \
    fi

# Ensure pip is installed
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get --no-install-recommends install -y \
    python3-pip

# Install Poetry
RUN pip install poetry

# Copy poetry files
COPY poetry.lock pyproject.toml ${APP_HOME}

# Install dependencies:
RUN poetry config virtualenvs.create false \
    && poetry install --with dev --no-interaction --no-ansi --no-root

# Copy remaining project files
COPY noxfile.py manage.py ${APP_HOME}
COPY .darglint .editorconfig .flake8 .gitignore .pre-commit-config.yaml .prettierignore .readthedocs.yml bandit.yml ${APP_HOME}
COPY CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md ${APP_HOME}
COPY ./docs/ ${APP_HOME}/docs
COPY ./example_project/ ${APP_HOME}/example_project/
COPY ./tests/ ${APP_HOME}/tests/
COPY ./src/ ${APP_HOME}/
COPY ./src/ ${APP_HOME}/src/

# Rehash pyenv shims
RUN pyenv rehash

# Project initialization:
COPY ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Initialize git and add .
RUN git init
RUN git add .

ENTRYPOINT ["/entrypoint"]
