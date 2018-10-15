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
import sys
sys.path.append("..")

from FileOperations import *


####################################################################################################################
# Test
####################################################################################################################
class TestFileOperations(unittest.TestCase):

    def setUp(self):
        shutil.rmtree("TestDir", ignore_errors=True)
        os.mkdir("TestDir")
        with open ("TestDir/FunnyBunny.txt", "w+") as f:
            f.write("Bunny")
        with open ("TestDir/FunnyBird.txt", "w+") as f:
            f.write("Bird")

    def tearDown(self):
        shutil.rmtree("TestDir")

    ### RemoveWithWildcard ###
    def testRemoveWithWildcard_One(self):
        RemoveWithWildcard("TestDir", ".*Bunny.*")
        files = os.listdir("TestDir")
        self.assertEqual(1, len(files))
        self.assertEqual("FunnyBird.txt", files[0])

    def testRemoveWithWildcard_Multiple(self):
        RemoveWithWildcard("TestDir", "Funny.*")
        files = os.listdir("TestDir")
        self.assertEqual(0, len(files))

    def testRemoveWithWildcard_None(self):
        RemoveWithWildcard("TestDir", ".*NotFound.*")
        files = os.listdir("TestDir")
        self.assertEqual(2, len(files))

    ### FindWithWildcard ###
    def testFindWithWildcard_One(self):
        files = FindWithWildcard("TestDir", ".*Bunny.*")
        self.assertEqual(["FunnyBunny.txt"], files)

    def testFindWithWildcard_Multiple(self):
        files = FindWithWildcard("TestDir", "Funny.*")
        self.assertEqual({"FunnyBunny.txt", "FunnyBird.txt"}, set(files))

    def testFindWithWildcard_None(self):
        files = FindWithWildcard("TestDir", ".*NotFound.*")
        self.assertEqual([], files)

    ### OpenWithWildcard ###
    def testOpenWithWildcard_One(self):
        with OpenWithWildcard("TestDir", ".*Bunny.*") as f:
            self.assertEqual(f.read(), "Bunny")

    def testOpenWithWildcard_Multiple(self):
        with self.assertRaises(Exception):
            OpenWithWildcard("TestDir", "Funny.*")

    def testOpenWithWildcard_None(self):
        with self.assertRaises(Exception):
            OpenWithWildcard("TestDir", ".*NotFound.*")

    def testOpenWithWildcard_Append(self):
        with OpenWithWildcard("TestDir", ".*Bunny.*", "a") as f:
            f.write(" Jumps")
        with open("TestDir/FunnyBunny.txt", "r") as f:
            self.assertEqual(f.read(), "Bunny Jumps")

