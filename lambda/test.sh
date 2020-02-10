#!/usr/bin/env bash

set -e

export PIPENV_IGNORE_VIRTUALENVS=1
export PIPENV_VENV_IN_PROJECT=1

pipenv install --dev

pipenv run python -m mypy_boto3 # Setup [s3,...] stubs
pipenv run mypy -p src.app

pipenv run python -m pytest
