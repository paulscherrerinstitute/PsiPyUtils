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

from TextReplace import *


####################################################################################################################
# Test
####################################################################################################################
class TestTextReplace_TaggedReplace(unittest.TestCase):

    TEST_FILE = "myTest.txt"

    def setUp(self):
        with open(self.TEST_FILE, "w+") as f:
            f.write("bla <st> any text <et> blubb")

    def tearDown(self):
        os.remove(self.TEST_FILE)

    def testNormal(self):
        TaggedReplace("<st>", "<et>", " rabbit ", "myTest.txt")
        with open(self.TEST_FILE) as f:
            contentAfter = f.read()
        self.assertEqual("bla <st> rabbit <et> blubb", contentAfter)

    def testFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            TaggedReplace("<st>", "<et>", " rabbit ", "IllegalFile.txt")

    def testTagsNotFound(self):
        with self.assertRaises(TagsNotFoundError):
            TaggedReplace("<s>", "<et>", " rabbit ", "myTest.txt")