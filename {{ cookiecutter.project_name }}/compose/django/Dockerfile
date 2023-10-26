FROM mcr.microsoft.com/playwright:v1.39.0-jammy

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app
ARG DEBIAN_FRONTEND=noninteractive

ARG PYTHON_3_9=3.9.18
ARG PYTHON_3_10=3.10.13
ARG PYTHON_3_11=3.11.6
ARG PYTHON_3_12=3.12.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install apt packages
RUN apt-get update
RUN apt-get install -y \
    # Some basic tools and libraries
    bash curl wget git make \
    build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    # psycopg2 dependencies
    libpq-dev

# Add symbolic link (python) to python3
# RUN ln -s /usr/bin/python3 /usr/bin/python

# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git /pyenv
ENV PYENV_ROOT /pyenv

# Add symbolic link to pyenv
RUN ln -s /pyenv/bin/pyenv /usr/bin/pyenv

# Install Python versions
RUN pyenv install ${PYTHON_3_12}
RUN pyenv install ${PYTHON_3_11}
RUN pyenv install ${PYTHON_3_10}
RUN pyenv install ${PYTHON_3_9}

# Initialize pyenv
RUN eval "$(pyenv init -)"

# Add deadsnakes PPA
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN add-apt-repository 'ppa:deadsnakes/ppa'

# Make Python version accessible in the project and install Python venv
RUN pyenv local ${PYTHON_3_9}
RUN apt-get update
RUN apt-get install -y python3.9-venv

# Make Python version accessible in the project and install Python venv
RUN pyenv local ${PYTHON_3_10}
RUN apt-get update
RUN apt-get install -y python3.10-venv

# Make Python version accessible in the project and install Python venv
RUN pyenv local ${PYTHON_3_12}
RUN apt-get update
RUN apt-get install -y python3.12-venv

# Make Python version accessible in the project and install Python venv
RUN pyenv local ${PYTHON_3_11}
RUN apt-get update
RUN apt-get install -y python3.11-venv

# Add symbolic link (python) to python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Ensure pip is installed
RUN apt-get install -y python3-pip

# Install Poetry
RUN pip install poetry

# copy application files
COPY noxfile.py poetry.lock pyproject.toml ${APP_HOME}
COPY .darglint .editorconfig .flake8 .gitignore .pre-commit-config.yaml .prettierignore .readthedocs.yml bandit.yml ${APP_HOME}
COPY CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md ${APP_HOME}

COPY ./docs/ ${APP_HOME}/docs
COPY ./example_project/ ${APP_HOME}/
COPY ./src/{{ cookiecutter.package_name }}/ ${APP_HOME}/{{ cookiecutter.package_name }}/
COPY ./tests/ ${APP_HOME}/tests/
COPY ./src/ ${APP_HOME}/src/

# Install dependencies:
RUN poetry config virtualenvs.create false \
    && poetry install --with dev --no-interaction --no-ansi --no-root

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
