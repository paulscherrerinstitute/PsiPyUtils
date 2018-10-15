##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################
import os
class FileWriter:
    """
    This class allows to easily generate text files with indentation.

    It is used as context object. Example below:

    with FileWriter("bla.txt") as file:
        file.WriteLn("anything")
    """
    ####################################################################################################################
    # Constructor
    ####################################################################################################################
    def __init__(self, fileName : str, indentChar : str = None, overwrite : bool = True):
        """
        Constructor

        :param fileName: Name of the file to create
        :type fileName: str
        :param indentChar: String to be used for indentation. By default this is a tab per indent. Hwoever, the user
                           can choose something else (e.g. two spaces per indent).
        :type indentChar: str
        """
        if not overwrite:
            if os.path.exists(fileName):
                raise FileExistsError("File {} already exists".format(fileName))
        self._fileName = fileName
        if indentChar is None:
            indentChar = "\t"
        self._indentChar = indentChar

    ####################################################################################################################
    # Context object handlers
    ####################################################################################################################
    def __enter__(self):
        self._indent = 0
        self._content = []
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self._fileName, "w+") as f:
            f.write("".join(self._content))

    ####################################################################################################################
    # Public Functions
    ####################################################################################################################
    def WriteLn(self, line : str = ""):
        """
        Write a line to the file. Before the first character, the currently active number of indentation characters is
        added. At the ned of the line, a linebreak is added.

        :param line: Line to tadd to the file
        :type line: str
        :return: Object the method is called on
        :rtype: FileWriter
        """
        ln = "".join([self._indentChar for i in range(self._indent)])
        ln += line
        ln += "\n"
        self._content.append(ln)
        return self

    def IncIndent(self):
        """
        Increase the indentation by one

        :return: Object the method is called on
        :rtype: FileWriter
        """
        self._indent += 1
        return self

    def DecIndent(self):
        """
        Decrease the indentation by one

        :return: Object the method is called on
        :rtype: FileWriter
        """
        self._indent -= 1
        return self

    def RemoveFromLastLine(self, chars : int, keepNewline : bool = True, append : str = ""):
        """
        Remove a number of character from the last line added.

        :param chars: Number of characters to remove (without line-break)
        :type chars: int
        :param keepNewline: True = line-break is preserved
                            False = line-break is removed
        :type keepNewline: bool
        :return: Object the method is called on
        :rtype: FileWriter
        """
        self._content[-1] = self._content[-1][:-1-chars]
        self._content[-1] = self._content[-1] + append
        if keepNewline:
            self._content[-1] = self._content[-1] + "\n"
        return self

