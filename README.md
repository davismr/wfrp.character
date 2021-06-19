Installation
============

[![Python application](https://github.com/davismr/wfrp.character/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/davismr/wfrp.character/actions/workflows/python-app.yml)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Create a Python virtual environment
-----------------------------------

```bash
python3 -m venv my_env
```

Activate virtual environment
----------------------------

```bash
. bin/activate
```

Upgrade packaging tools
-----------------------

```bash
pip install --upgrade pip setuptools
```

Install the project in editable mode with its testing requirements
------------------------------------------------------------------

```bash
pip install -e .[testing]
```

Run the tests
-------------

```bash
pytest
```

Run the project
---------------

```bash
pserve development.ini
```
