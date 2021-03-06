#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


import os
import sys


tcldir = os.path.join(sys._MEIPASS, 'tcl')
tkdir = os.path.join(sys._MEIPASS, 'tk')

if not os.path.isdir(tcldir):
    raise FileNotFoundError('Tcl data directory "%s" not found.' % (tcldir))
if not os.path.isdir(tkdir):
    raise FileNotFoundError('Tk data directory "%s" not found.' % (tkdir))

# Notify "tkinter" of such directories.
os.environ["TCL_LIBRARY"] = tcldir
os.environ["TK_LIBRARY"] = tkdir
