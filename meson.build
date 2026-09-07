#
# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2023-present Gene C <arch@sapience.com>
#

project('pyconcurrent', ['c'],
  version: files('src/version.txt'),
  meson_version: '>=1.10.0',
  default_options: [
    'c_std=c23',
    'warning_level=3',
    'b_pie=true',
    'prefix=/usr',
    'mandir=share/man',
    ],
)

d_etc = get_option('sysconfdir')
d_lib = get_option('libdir')
d_bin = get_option('bindir')
d_man = get_option('mandir')
d_share = get_option('datadir')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
proj_root = meson.project_source_root()
py_dep = py.dependency(embed: true)

inc_dir = []
lib_sources = []

#
# top-level files
#

#
# Python submodules
#
subdir('src/pyconcurrent')

#
# Deps
#

#
# Executables
#

#
# Install
#

s_license = 'src/data/license'
s_changelog = 'src/data/changelog'
s_docs = 'src/data/docs'
s_examples = 'src/data/examples'
s_scripts = 'src/scripts'
manual = 'pyconcurrent.pdf'

# 
# /usr/share/pyconcurrent/docs
# 
install_data(
  [
    s_docs / manual,
  ],
  install_dir: d_share / 'pyconcurrent/docs'
)

install_subdir(
  [
    s_docs / 'html',
  ],
  install_dir: d_share / 'pyconcurrent/docs',
  strip_directory: false
)

# 
# /usr/share/pyconcurrent 
# 
install_data(
  [
    'README.rst',
    s_changelog / 'Changelog.rst',
    'packaging/Changelog',
  ],
  install_dir: d_share / 'pyconcurrent'
)

# 
# /usr/share/licenses/pyconcurrent 
# 
install_data(
  [
    s_license / 'License-gpl-2.0.txt',
    s_license / 'License.rst',
  ],
  install_dir: d_share / 'licenses/pyconcurrent'
)

#
# Tests
#
pytest = find_program('pytest')
srcdir = proj_root / 'src'
testdir = srcdir / 'tests'

test_files = [
  'test_asyncio.py',
  'test_mp.py',
  'test_run_prog.py',
]

foreach this_test : test_files
  test(this_test,
    pytest,
    args: [testdir / this_test],
    env: {'PYTHONPATH': srcdir},
    suite: ['unit'],
    timeout: 60,
  )
endforeach

#test('tests',
#  pytest,
#  args: [src_root / 'src/tests'],
#  env: {'PYTHONPATH': meson.project_source_root()},
#  suite: 'pytest',
#  timeout: 120,
#)   

