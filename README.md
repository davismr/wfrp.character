# Installation

[![Python application](https://github.com/davismr/wfrp.character/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/davismr/wfrp.character/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/davismr/wfrp.character/branch/main/graph/badge.svg?token=8U307XOQEW)](https://codecov.io/gh/davismr/wfrp.character)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Warhammer Fantasy Roleplay 4th Edition Copyright Games Workshop and licensed to Cubicle 7 Entertainment Limited.
All content is copyright their respective authors.

## Create a Python virtual environment

```bash
python3 -m venv my_env
```

## Activate virtual environment

```bash
. bin/activate
```

## Upgrade packaging tools

```bash
pip install --upgrade pip setuptools
```

## Install the project in editable mode with its testing requirements

```bash
pip install -e .[testing]
```

## Run the tests

```bash
pytest
```

## Run the project
Initialise the database, this will silently not do anything if a db already exists.
You have to delete the db and re-initialise on any db structure change. There is no db
migration facility yet.
```bash
init_db development.ini
```

```bash
pserve development.ini
```

## Installing Weasyprint
This is only used for generating the PDFs

Use MacPorts as detailed here:
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

If you get OSError due to missing libraries, you may need to export the library locations.

```bash
export DYLD_FALLBACK_LIBRARY_PATH=/opt/local/lib:$DYLD_FALLBACK_LIBRARY_PATH
```
