import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as infile:
    README = infile.read()
with open(os.path.join(here, "docs", "HISTORY.md")) as infile:
    CHANGES = infile.read()

requires = [
    "deform",
    "pyramid",
    "pyramid_chameleon",
    "pyramid_debugtoolbar",
    "pyramid_tm",
    "sqlalchemy",
    "waitress",
    "zope.sqlalchemy",
]

tests_require = [
    "black",
    "flake8",
    "isort",
    "pre-commit",
    "WebTest >= 1.3.1",
    "pytest >= 3.7.4",
    "pytest-cov",
]

setup(
    name="wfrp.character",
    description="Character generator for Warhammer Fantasy Roleplay Version 4.",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="Michael Davis",
    author_email="m.r.davis@me.com",
    url="",
    keywords="web pyramid pylons",
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require},
    install_requires=requires,
    entry_points={
        "paste.app_factory": ["main = wfrp.character.application:main"],
        "console_scripts": ["init_db = wfrp.character.init_db:main"],
    },
)
