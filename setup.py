from cx_Freeze import setup, Executable

import sys
base = "Win32GUI" if sys.platform == 'win32' else None

## Don't remember why I needed this
#import os
#os.environ['TCL_LIBRARY'] = r'C:\WinPython\python-3.6.5.amd64\tcl\tcl8.6'
#os.environ['TK_LIBRARY'] = r'C:\WinPython\python-3.6.5.amd64\tcl\tk8.6'

executables = [
    Executable('glitchgui.py', base=base)
]

buildOptions = dict(
    packages = [ '_cffi_backend', 'idna', 'queue', 'requests'],
    excludes = [],
    includes = [],
    include_files = []
)

setup(
    name='pyglitch',
    version='0.1',
    packages=[],
    url='https://glitch.sharky.pw',
    license='Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International',
    author='Sharky',
    author_email='sharky@sharky.pw',
    description='For glitching things, yo!',
    options=dict(build_exe = buildOptions),
    executables=executables
)
