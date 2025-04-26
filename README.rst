.. SPDX-License-Identifier: MIT

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

New release. 

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

This example uses asyncio and subprocesses to call an executable.
*tasks* must be a list of *(key, arg)* pairs, 1 per task. 

*key* is a unique identifier, used by calleer, one per task. *arg* is an additional argument 
for each task; typicall whatever work that task is responsible for. 
Each result returned contains both the *key* and the *arg* used by that task.

This example has 5 tasks to be run concurrently, at most 4 at a time. The results are 
available in the *proc_run.result*, which is a list of *ProcResult* items; one per task.
Since the result order is not pre-defined, each task is identifiable by it's *key* available 
in the : *result.key*.

 .. code-block:: python

    #!/usr/bin/python

    import asyncio
    from pyconcurrent import ProcRunAsyncio

    async def main():
        """pargs can have additional arguments."""
        pargs = ['/usr/bin/sleep']       
        tasks = [(1, 1), (2,7), (3,2), (4, 2), (5, 1)]

        proc_run = ProcRunAsyncio(pargs, tasks, num_workers=4, timeout=30)
        await proc_run.run_all()
        proc_run.print_results()

    if __name__ == '__main__':
        asyncio.run(main())

To switch to *multiprocessing* simply replace *ProcRunAsyncio* with  *ProcRunMp*, 
and drop *await* since MP is not *async*. i.e.

 .. code-block:: python

    #!/usr/bin/python

    from pyconcurrent import ProcRunMp

    def main()
        pargs = ['/usr/bin/sleep']
        tasks = [(1, 1), (2,7), (3,2), (4, 2), (5, 1)]

        proc_run = ProcRunMp(pargs, tasks, num_workers=4, timeout=30)
        proc_run.run_all()
        proc_run.print_results()

    if __name__ == '__main__':
        main()

The next example uses a caller supplied function together with asyncio. As in the first
example, there are 5 tasks to do and the number of workers is 4, so that 4 tasks 
are permitted to be run simultaneously.

 .. code-block:: python
    
    #!/usr/bin/python

    import asyncio
    from pyconcurrent import ProcRunAsyncio

    async def test_func_async(key, args) -> (bool, []):
        """return 2-tuple (success, result)."""
        success = True
        nap = args[-1]              # pull off the last argument
        await asyncio.sleep(nap)
        answer = {
                'key' : key,
                'args' : args,
                'success' : success,
                'result' : 'test_func done',
              }
        return (success, answer)

    async def main():
        pargs = [test_func_async, 'dummy-arg']
        tasks = [(1, 1), (2,7), (3,2), (4, 2), (5, 1)]

        proc_run = ProcRunAsyncio(pargs, tasks, num_workers=4, timeout=30)
        await proc_run.run_all()
        proc_run.print_results()

    if __name__ == '__main__':
        asyncio.run(main())

For equivalent multiprocessor version for this one, same as above, simply replace *ProcRunAsyncio* 
with *ProcRunMp* and drop any references to **async/await**.

The caller supplied function here, *test_func_async()*, must return a 2-tuple 
of *(success:bool, answer:Any)* where success should be *True* if function succeeded.

The function may optionally raise a *RuntimeError* exception, but typically setting *success*
is sufficient. If you are using execptions then please use this one.

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
 * hatch           (aka python-hatch)
 * wheel           (aka python-wheel)
 * build           (aka python-build)
 * installer       (aka python-installer)
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

We follow the *live at head commit* philosophy. This means we recommend using the
latest commit on git master branch. We also provide git tags. 

This approach is also taken by Google [1]_ [2]_.

License
=======

Created by Gene C. and licensed under the terms of the MIT license.

* SPDX-License-Identifier: MIT
* SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>

.. _Github: https://github.com/gene-git/pyconcurrent
.. _Archlinux AUR: https://aur.archlinux.org/packages/pyconcurrent

.. [1] https://github.com/google/googletest  
.. [2] https://abseil.io/about/philosophy#upgrade-support


