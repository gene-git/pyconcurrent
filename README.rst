.. SPDX-License-Identifier: GPL-2.0-or-later

============
pyconcurrent
============

Overview
========

pyconcurrent is a python class that provides a simple way to do concurrent processing.
It supports both asyncio and multiprocessing. The tasks to be run concurrently
can either be an executable which is run as a subprocess or a python function to be called.

Key features
------------

* Provides two classes to do the work:
  *ProcRunAsyncio* and *ProcRunMp*

* Results are provided by the *results* attribute in each class. 
  This is a list of *ProcResults*; one per run.

* Documentation includes the API reference.

* pytest classes validate that all functionality works as it should.

Documentation
-------------

The manual provides detailed information and is available in both HTML and PDF formats.
Both are installed under */usr/share/pyconcurrent/docs*.

The manual is also available at: `readthedocs <https://pyconcurrent.readthedocs.io>`_.


Signed Source
=============

All git tags are signed with arch@sapience.com key which is available via WKD
or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
The key is included in the Arch package and the source= line with *?signed* at the end can be used
to verify the git tag.  You can also manually verify the signature
using manually verify using *git tag -v <tag-name>*

pyconcurrent module
===================

Please see the API reference manual for details.
The manual, available in both PDF and html, has illustrative examples using:

* ProcRunAsyncio class
* ProcRunMp class
* run_prog


