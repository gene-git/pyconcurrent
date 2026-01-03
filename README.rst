.. SPDX-License-Identifier: GPL-2.0-or-later

############
pyconcurrent
############

Overview
========

pyconcurrent is a python class that provides a simple way to do concurrent processing.
It supports both asyncio and multiprocessing. The tasks to be run concurrently
can either be an executable which is run as a subprocess or a python function to be called.

Key features
============

* Provides two classes to do the work:
  *ProcRunAsyncio* and *ProcRunMp*

* Results are provided by the *results* attribute in each class. 
  This is a list of *ProcResults*; one per run.

* Documentation includes the API reference.

* pytest classes validate that all functionality works as it should.

New / Interesting
==================

* switch python packaging from hatch to uv.
* New function run_prog() to run external command. Strictly speaking, this has nothing to do with 
  concurrency, but doing this robustly can be a little tricky. So it is included here.
* PEP 561: Mark module as typed. Now *mypy* run on code using this module will have the type hints.
* Asyncio now uses the recommended TaskGroup class together with 
  the timeout() context manager. These were introduced in python 3.11. 
  This newer approach is cleaner, more robust and ensures all tasks 
  are appropriately cancelled in the event one task fails. It also offers
  superior timeout capabilities.
* Timeout now works when using a caller provided function
  in addition to subprocesses.

###############
Getting Started
###############

All git tags are signed with arch@sapience.com key which is available via WKD
or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
The key is included in the Arch package and the source= line with *?signed* at the end can be used
to verify the git tag.  You can also manually verify the signature

pyconcurrent module
===================

Please see the API reference for additional details.

Here are a couple of simple examples illustrating how the module can be used.

Example 1a: Asyncio
-------------------

This example uses asyncio and subprocesses to call an executable.
*tasks* must be a list of *(key, arg)* pairs, 1 per task. 

*key* is a unique identifier, used by caller, one per task. *arg* is an additional argument 
for each task; typically *arg* provides for whatever work that task is responsible for. 
Each *result* returned contains both the *key* and the *arg* used by that task, 
information about the success of the task as well as any outputs produced by the task.
See *ProcResult* class for more detail.

This example has 5 tasks to be run concurrently, at most 4 at a time. The results are 
available in the *proc_run.result*, which is a list of *ProcResult* items; one per task.
Since the result order is not pre-defined, each task is identifiable by it's *key* available 
in the : *result.key*.

.. literalinclude:: examples/example_1a.py
   :language: python
   :caption: Example 1a


Example 1b: Multiprocessing
---------------------------

To switch to *multiprocessing* simply replace *ProcRunAsyncio* with  *ProcRunMp*, 
and drop *await* since MP is not *async*. i.e.

.. literalinclude:: examples/example_1b.py
   :language: python
   :caption: Example 1b

Example 2: Asnycio
------------------

The next example uses a caller supplied function together with asyncio. As in the first
example, there are 5 tasks to do and the number of workers is 4, so that 4 tasks 
are permitted to be run simultaneously.

.. literalinclude:: examples/example_2.py
   :language: python
   :caption: Example 2

For equivalent multiprocessor version for this one, same as above, simply replace *ProcRunAsyncio* 
with *ProcRunMp* and drop any references to **async/await**.

The caller supplied function here, *test_func_async()*, must return a 2-tuple 
of *(success:bool, answer:Any)* where success should be *True* if function succeeded.

The function may optionally raise a *RuntimeError* exception, but typically setting *success*
is sufficient. If you are using exceptions then please use this one.

Example 3: Non-concurrent
-------------------------

This one shows a non-concurrent external program being executed.

.. literalinclude:: examples/example_3.py
   :language: python
   :caption: Example 3


########
Appendix
########

Installation
============

Available on
 * `Github`_
 * `Archlinux AUR`_

On Arch you can build using the provided PKGBUILD in the packaging directory or from the AUR.
All git tags are signed with arch@sapience.com key which is available via WKD
or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
The key is included in the Arch package and the source= line with *?signed* at the end can be used
to verify the git tag.  You can also manually verify the signature

.. code-block:: bash

    git tag -v <tag-name>

To build manually, clone the repo and :

 .. code-block:: bash

    rm -f dist/*
    /usr/bin/python -m build --wheel --no-isolation
    root_dest="/"
    ./scripts/do-install $root_dest

When running as non-root then root_dest must be a user writable directory

Dependencies
============

**Run Time** :

 * python          (3.13 or later)

**Building Package** :

* git
* uv
* uv_build        (aka python-uv-build)
* rsync
* pytest          (aka python-pytest)
* pytest-asyncio  (aka python-pytest-asyncio)

**Optional for building docs** :

* sphinx
* myst-parser      (aka python-myst-parser)
* sphinx-autoapi   (aka python-sphinx-autoapi)
* texlive-latexextra (archlinux packaging of texlive tools)

Philosophy
==========

We follow the *live at head commit* philosophy as recommended by
Google's Abseil team [1]_.  This means we recommend using the
latest commit on git master branch. 


License
=======

Created by Gene C. and licensed under the terms of the GPL-2.0-or-later license.

* SPDX-License-Identifier: GPL-2.0-or-later
* SPDX-FileCopyrightText: © 2025-present Gene C <arch@sapience.com>

.. _Github: https://github.com/gene-git/pyconcurrent
.. _Archlinux AUR: https://aur.archlinux.org/packages/pyconcurrent

.. [1] https://abseil.io/about/philosophy#upgrade-support


