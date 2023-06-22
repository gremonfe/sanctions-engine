import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'packages': ['requests'],
    'excludes': ['tkinter'],
    'include_files': ['config.json']
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable('sanctions_validation.py', base=base)]

setup(name='SanctionsValidator',
      version='0.1',
      description='Sanctions Validator App',
      options={'build_exe': build_exe_options},
      executables=executables)
