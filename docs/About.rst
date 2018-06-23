.. image:: https://raw.githubusercontent.com/senaite/senaite.api/master/static/api-logo.png
   :alt: senaite.api
   :height: 64 px
   :align: center

- **SENAITE.API**: *The Swiss-Army-Knife for SENAITE Core and Add-on developers*

.. image:: https://img.shields.io/pypi/v/senaite.api.svg?style=flat-square
   :target: https://pypi.python.org/pypi/senaite.api

.. image:: https://img.shields.io/github/issues-pr/senaite/senaite.api.svg?style=flat-square
   :target: https://github.com/senaite/senaite.api/pulls

.. image:: https://img.shields.io/github/issues/senaite/senaite.api.svg?style=flat-square
   :target: https://github.com/senaite/senaite.api/issues

.. image:: https://img.shields.io/badge/README-GitHub-blue.svg?style=flat-square
   :target: https://github.com/senaite/senaite.api#readme

About
=====

SENAITE API is the Swiss-Army-Knife for SENAITE Core and Add-on developers. It
provides a sane interface for common tasks in SENAITE, like e.g. object
creation, lookup by ID/UID, search etc.

Please see the doctests for further details and usage:

-  `Core API Documentation`_
-  `Analysis API Documentation`_


Installation
============

Please follow the installations instructions for `Plone 4`_ and
`senaite.lims`_.

To install SENAITE API, you have to add `senaite.api` into the
`eggs` list inside the `[buildout]` section of your
`buildout.cfg`::

   [buildout]
   parts =
       instance
   extends =
       http://dist.plone.org/release/4.3.17/versions.cfg
   find-links =
       http://dist.plone.org/release/4.3.17
       http://dist.plone.org/thirdparty
   eggs =
       Plone
       Pillow
       senaite.lims
       senaite.api
   zcml =
   eggs-directory = ${buildout:directory}/eggs

   [instance]
   recipe = plone.recipe.zope2instance
   user = admin:admin
   http-address = 0.0.0.0:8080
   eggs =
       ${buildout:eggs}
   zcml =
       ${buildout:zcml}

   [versions]
   setuptools =
   zc.buildout =


**Note**

The above example works for the buildout created by the unified
installer. If you however have a custom buildout you might need to add
the egg to the `eggs` list in the `[instance]` section rather than
adding it in the `[buildout]` section.

Also see this section of the Plone documentation for further details:
https://docs.plone.org/4/en/manage/installing/installing_addons.html

**Important**

For the changes to take effect you need to re-run buildout from your
console::

   bin/buildout


.. _Plone 4: https://docs.plone.org/4/en/manage/installing/index.html
.. _senaite.lims: https://github.com/senaite/senaite.lims#installation
.. _Core API Documentation: https://github.com/senaite/senaite.api/blob/master/src/senaite/api/docs/API.rst
.. _Analysis API Documentation: https://github.com/senaite/senaite.api/blob/master/src/senaite/api/docs/API_analysis.rst
