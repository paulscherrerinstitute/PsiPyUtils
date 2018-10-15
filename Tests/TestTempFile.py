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
import shutil

from TempFile import TempFile

####################################################################################################################
# Test
####################################################################################################################
class TestTempFile(unittest.TestCase):

    TEST_FILE = "tempFile.txt"

    def testNormalFileOperations(self):
        #Create file and copy content
        with TempFile(self.TEST_FILE) as f:
            f.write("FunnyTest")
            f.flush()
            shutil.copy(self.TEST_FILE, "check.txt")
        self.assertFalse(self.TEST_FILE in os.listdir())
        self.assertTrue("check.txt" in os.listdir())
        with open("check.txt") as f:
            content = f.read()
        self.assertEqual(content, "FunnyTest")
        os.remove("check.txt")





