=========
Changelog
=========

Tags
====

::

	1.1.2 (2025-04-24) -> 2.5.0 (2025-06-19)
	40 commits.

Commits
=======


* 2025-06-19  : **2.5.0**

::

                run_prog: make stdin nonblock as well
 2025-06-17     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-17  : **2.4.1**

::

                PEP-484 use builtin tuple instead of Tuple
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-06-17  : **2.4.0**

::

                New function run_prog() to run external command.
 2025-05-21     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-21  : **2.3.0**

::

                Use builtin types where possible. e.g. typing.List -> list
 2025-05-19     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-19  : **2.2.3**

::

                Arch PKGBUILD: move pytest dependency from makedepends to checkdepends.
 2025-05-03     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-03  : **2.2.2**

::

                Remove old test directory
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-03  : **2.2.1**

::

                pytests: reorganize a little. tests are unchanged
 2025-05-01     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-05-01  : **2.2.0**

::

                PEP 561 type hints (module users using mypy etc get type hints)
                Update status to Production/Stable
 2025-04-30     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-30  : **2.1.0**

::

                Bug fix returning stdout string from subprocess
 2025-04-27     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-27  : **2.0.2**

::

                API ref rst format
                Fix typo in api reference

* 2025-04-27  : **2.0.0**

::

                Asyncio now uses the recommended TaskGroup class together with
                   the timeout() context manager. These were introduced in python 3.11.
                   This newer approach is cleaner, more robust and ensures all tasks
                   are appropriately cancelled in the event one task fails. It also offers
                   superior timeout capabilities.
                Timeout now works when using a caller provided function in addition to
                subprocesses.
 2025-04-26     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-26  : **1.5.0**

::

                Style per PEP-8, PEP-257 and PEP-484.
                Bug fix with stdout/stderr returned for asyncio using subprocesses
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-26  : **1.4.1**

::

                More consistent with PEP-8 & PEP-257.
                  Primarily double quotes for docstrings instead of single and ensure ends
                  with period.
 2025-04-25     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-25  : **1.4.0**

::

                asyncio : missing decode() for stdout/err
                pytest : ensure python path uses dev source for tests
                Add missing SPDX identifiers
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-25  : **1.3.3**

::

                Fix readme typo and small tweak for clarity
 2025-04-24     update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.3.2**

::

                Change examples in README to include everything to actually run
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.3.1**

::

                Add note about git signing key in readme
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.3.0**

::

                Add missing tests dir after it was moved
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.2.0**

::

                Move tests dir to top level
                update Docs/Changelogs Docs/_build/html Docs/pyconcurrent.pdf

* 2025-04-24  : **1.1.3**

::

                Add dateutil dep to PKGBUILD

* 2025-04-24  : **1.1.2**

::

                Initial Commit


