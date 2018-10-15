##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################
import os

class TempWorkDir:
    """
    This class allows changing the directory for only a few lines of python script code and switch back to the old
    location afterwards automatically

    Usage example:
        with TempWorkFid("../otherDir"):
            #do some stuff
    """
    def __init__(self, dir : str):
        self._dir = dir

    def __enter__(self):
        self._prevDir = os.path.abspath(os.curdir)
        os.chdir(self._dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._prevDir)


