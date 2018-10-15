##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################
import os
import re
from typing import List

def RemoveWithWildcard(dir : str, pattern : str):
    """
    Remove files from a directory whoes name does match a regex pattern.

    Note that the function does not recurse into subdirectories.

    :param dir:         Directory to remove files from (child directories are not scanned)
    :param pattern:     python regex pattern (.* means any number of any characters)
    """
    for file in os.listdir(dir):
        if re.search(pattern, file):
            os.remove(os.path.join(dir, file))

def FindWithWildcard(dir : str, pattern : str) -> List[str]:
    """
    Return all filenames in a directory that match a regex pattern.

    Note that the function does not recurse into subdirectories.

    :param dir:         Directory to remove files from (child directories are not scanned)
    :param pattern:     python regex pattern (.* means any number of any characters)
    :return:            List of file-names
    """
    l = []
    for file in os.listdir(dir):
        if re.search(pattern, file):
            l.append(file)
    return l

def OpenWithWildcard(dir : str, pattern : str, mode : str = "r"):
    """
    Open a file in a directory that matches a regex pattern. If the pattern is ambigious (matches multiple files), an
    exception is risen.

    :param dir:         Directory to find the file in
    :param pattern:     python regex pattern (.* means any number of any characters)
    :param mode:        File open mode
    :return:            File object
    """
    fileName = FindWithWildcard(dir, pattern)
    if len(fileName) > 1:
        raise Exception("\n    ".join(["Pattern matches more than one file: "] + fileName))
    if len(fileName) < 1:
        raise Exception("Pattern does not match any file")
    return open(os.path.join(dir, fileName[0]), mode=mode)

def AbsPathLinuxStyle(path : str) -> str:
    """
    This function returns an absolute path in linux style (forward slashes), also if it is executed on Windows.
    This is very useful for tools that use linux paths even if they run on windows (e.g. SDK, Vivado, etc.)

    :param path: Relative or absolute path in Linux or Windows style
    :return: Absolute path in Linux style
    """
    return os.path.abspath(path).replace("\\", "/")