# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "1.2.2"

with open("docs/About.rst", "r") as fh:
    long_description = fh.read()

with open("src/senaite/api/docs/API.rst", "r") as fh:
    long_description += "\n\n"
    long_description += "Core API\n"
    long_description += "========\n"
    long_description += fh.read()

with open("src/senaite/api/docs/API_analysis.rst", "r") as fh:
    long_description += "\n\n"
    long_description += "Analysis API\n"
    long_description += "============\n"
    long_description += fh.read()

with open("docs/Changelog.rst", "r") as fh:
    long_description += "\n\n"
    long_description += "Changelog\n"
    long_description += "=========\n"
    long_description += fh.read()

setup(
    name="senaite.api",
    version=version,
    description="SENAITE API",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope2",
    ],
    keywords="",
    author="SENAITE Foundation",
    author_email="hello@senaite.com",
    url="https://github.com/senaite/senaite.api",
    license="GPLv2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    namespace_packages=["senaite"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "plone.api",
        "senaite.core",
    ],
    extras_require={
        "test": [
            "Products.PloneTestCase",
            "Products.SecureMailHost",
            "plone.app.robotframework",
            "plone.app.testing",
            "robotframework-debuglibrary",
            "robotframework-selenium2library",
            "robotsuite",
            "unittest2",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
