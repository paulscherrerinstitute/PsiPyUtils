##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################
import os


class TempFile:
    """
    This class allows creating a temporary file that only lives during a few lines of python script code. After exiting
    the with statement, the file is deleted automatically.

    Usage example:
        with TempFile("bla.txt") as f:
            f.write("text")
            f.flush()
            os.system("aCommand bla.txt")
    """

    def __init__(self, name : str):
        self._name = name

    def __enter__(self):
        self.f = open(self._name, "w+")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        os.remove(self._name)

    def __call__(self, *args, **kwargs):
        return self.f


