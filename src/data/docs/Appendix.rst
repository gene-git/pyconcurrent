.. SPDX-License-Identifier: GPL-2.0-or-later

========
Appendix
========

Installation
============

Available on
 * `Github <https://github.com/gene-git/pyconcurrent>`_
 * `Archlinux AUR <https://aur.archlinux.org/packages/python-pyconcurrent>`_

On Arch you can build using the provided PKGBUILD in the packaging directory or from the AUR.
All git tags are signed with arch@sapience.com key which is available via WKD
or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
The key is included in the Arch package and the source= line with *?signed* at the end can be used
to verify the git tag.  You can also manually verify the signature::

    git tag -v <tag-name>

To build manually, clone the repo and ::

    ./scripts/do-build
    ./scripts/do-install <destination-dieectory>

Dependencies
============

**Run Time** :

 * python          (3.14 or later)
 * dateutil

**Building Package** :

* git
* meson
* meson-python
* rsync
* pytest
* pytest-asyncio

License
=======

Created by Gene C. and licensed under the terms of the GPL-2.0-or-later license.

* SPDX-License-Identifier: GPL-2.0-or-later
* SPDX-FileCopyrightText: © 2025-present Gene C <arch@sapience.com>

