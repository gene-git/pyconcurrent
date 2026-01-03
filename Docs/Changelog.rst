Changelog
=========

Tags
====

.. code-block:: text

	1.1.2 (2025-04-24) -> 2.12.0 (2026-01-03)
	54 commits.

Commits
=======


* 2026-01-03  : **2.12.0**

.. code-block:: text

              - Add some uv installer options to install script
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2026-01-03  : **2.11.0**

.. code-block:: text

              - Actualy make the hatch to uv changes (oops)
                Change license to GPL-2.0-or-later
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2026-01-03  : **2.10.1**

.. code-block:: text

              - Change packaging from hatch to uv
                Some Doc updates
                Arch package keep python version requirement at 3.13+ for now.
 2025-06-26   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-26  : **2.9.0**

.. code-block:: text

              - run_prog: Make sure iolists are updated before calling select()
 2025-06-22   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-22  : **2.8.0**

.. code-block:: text

              - run_prog - make internal helper class internal so not included in API ref
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-22  : **2.7.0**

.. code-block:: text

              - run_prog: refactor code. Protect against one possible deadlock
 2025-06-19   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-19  : **2.6.0**

.. code-block:: text

              - run_prog: When writing to subprocess stdin, add a flush() before we close the file object
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-19  : **2.5.0**

.. code-block:: text

              - run_prog: make stdin nonblock as well
 2025-06-17   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-17  : **2.4.1**

.. code-block:: text

              - PEP-484 use builtin tuple instead of Tuple
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-17  : **2.4.0**

.. code-block:: text

              - New function run_prog() to run external command.
 2025-05-21   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-21  : **2.3.0**

.. code-block:: text

              - Use builtin types where possible. e.g. typing.List -> list
 2025-05-19   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-19  : **2.2.3**

.. code-block:: text

              - Arch PKGBUILD: move pytest dependency from makedepends to checkdepends.
 2025-05-03   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-03  : **2.2.2**

.. code-block:: text

              - Remove old test directory
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-03  : **2.2.1**

.. code-block:: text

              - pytests: reorganize a little. tests are unchanged
 2025-05-01   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-01  : **2.2.0**

.. code-block:: text

              - PEP 561 type hints (module users using mypy etc get type hints)
                Update status to Production/Stable
 2025-04-30   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-30  : **2.1.0**

.. code-block:: text

              - Bug fix returning stdout string from subprocess
 2025-04-27   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-27  : **2.0.2**

.. code-block:: text

              - API ref rst format
              - Fix typo in api reference

* 2025-04-27  : **2.0.0**

.. code-block:: text

              - Asyncio now uses the recommended TaskGroup class together with
                   the timeout() context manager. These were introduced in python 3.11.
                   This newer approach is cleaner, more robust and ensures all tasks
                   are appropriately cancelled in the event one task fails. It also offers
                   superior timeout capabilities.
                Timeout now works when using a caller provided function in addition to subprocesses.
 2025-04-26   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-26  : **1.5.0**

.. code-block:: text

              - Style per PEP-8, PEP-257 and PEP-484.
                Bug fix with stdout/stderr returned for asyncio using subprocesses
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-26  : **1.4.1**

.. code-block:: text

              - More consistent with PEP-8 & PEP-257.
                  Primarily double quotes for docstrings instead of single and ensure ends with period.
 2025-04-25   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-25  : **1.4.0**

.. code-block:: text

              - asyncio : missing decode() for stdout/err
                pytest : ensure python path uses dev source for tests
                Add missing SPDX identifiers
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-25  : **1.3.3**

.. code-block:: text

              - Fix readme typo and small tweak for clarity
 2025-04-24   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.3.2**

.. code-block:: text

              - Change examples in README to include everything to actually run
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.3.1**

.. code-block:: text

              - Add note about git signing key in readme
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.3.0**

.. code-block:: text

              - Add missing tests dir after it was moved
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.2.0**

.. code-block:: text

              - Move tests dir to top level
              - update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.1.3**

.. code-block:: text

              - Add dateutil dep to PKGBUILD

* 2025-04-24  : **1.1.2**

.. code-block:: text

              - Initial Commit


