##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################
import os
import sys

def AddToPathVariable(variable : str, path : str):
    """
    Add a value to a path variable if the value is not already present. If the variable does not exist it is created.

    Paths are automatically converted from/to Linux/Windows style

    :param variable: Name of the variable
    :param path: Path to add
    """
    #Get OS Settings
    if sys.platform.startswith("win"):
        varSep = ";"
        repFrom = "/"
        repTo = "\\"
    elif sys.platform.startswith("linux"):
        varSep = ":"
        repFrom = "\\"
        repTo = "/"
    else:
        raise Exception("OS Not Supported")
    #Convert Path
    pathConv = path.replace(repFrom, repTo)

    #If variable does not yet exist, create it
    if variable not in os.environ:
        os.environ[variable] = pathConv
        return

    #Check if path is already in os variable and return if this is the case
    if pathConv in os.environ[variable].split(varSep):
        return

    #Otherwise append
    os.environ[variable] += "{}{}".format(varSep, pathConv)

