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

from TempWorkDir import TempWorkDir

####################################################################################################################
# Test
####################################################################################################################
class TestTempWorkDir(unittest.TestCase):

    def setUp(self):
        os.mkdir("TestDir")
        f = open("TestDir/TestFile.txt", "w+")
        f.close()

    def tearDown(self):
        shutil.rmtree("TestDir", ignore_errors=True)

    def testOperation(self):
        prevPath = os.path.abspath(os.curdir)
        with TempWorkDir("TestDir"):
            self.assertTrue("TestFile.txt" in os.listdir())
            self.assertEqual(os.path.join(prevPath, "TestDir"), os.path.abspath(os.curdir))
        self.assertFalse("TestFile.txt" in os.listdir())
        self.assertEqual(prevPath, os.path.abspath(os.curdir))







