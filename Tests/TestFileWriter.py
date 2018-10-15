##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################

####################################################################################################################
# Imports
####################################################################################################################
import os
import unittest
import sys
sys.path.append("..")

from FileWriter import FileWriter


####################################################################################################################
# Test
####################################################################################################################
class TestFileWriter(unittest.TestCase):

    TEST_FILE = "myTest.txt"

    def tearDown(self):
        os.remove(self.TEST_FILE)

    def testNormal(self):
        with FileWriter(self.TEST_FILE) as f:
            f.WriteLn("a").IncIndent()
            f.WriteLn("b").DecIndent().WriteLn("c")

        with open(self.TEST_FILE) as file:
            lines = file.readlines()
        self.assertEqual("a\n", lines[0])
        self.assertEqual("\tb\n", lines[1])
        self.assertEqual("c\n", lines[2])


    def testRemoveFromLastLine(self):
        with FileWriter(self.TEST_FILE) as f:
            f.WriteLn("abc")
            f.WriteLn("def")
            f.RemoveFromLastLine(1)
            f.WriteLn("123")

        with open(self.TEST_FILE) as file:
            lines = file.readlines()
        self.assertEqual("abc\n", lines[0])
        self.assertEqual("de\n", lines[1])
        self.assertEqual("123\n", lines[2])