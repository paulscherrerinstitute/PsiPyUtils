import sys
import unittest
sys.path.append("..")

from XmlToolbox import XmlToolbox

####################################################################################################################
# Test
####################################################################################################################
class TestXmlToolbox(unittest.TestCase):

    TEST_FILE = "TestXmlToolbox.xml"

    def testSearch(self):
        #with XmlToolbox(self.TEST_FILE) as f:
        f = XmlToolbox(self.TEST_FILE)
        attr_value = f.get_attr_value_by_other_attr("./MODULES/MODULE", "IPTYPE", "PROCESSOR", "INSTANCE")
        self.assertEqual("ppc440_inst",attr_value)
        attr_value = f.get_attr_value_by_other_attr("./MODULES/MODULE/PARAMETERS/PARAMETER", "CHANGEDBY", "SYSTEM", "MPD_INDEX")
        self.assertEqual("0",attr_value)
        tag_value = f.get_tag_value("./MODULES/MODULE/DESCRIPTION")
        self.assertEqual("Clock Generator",tag_value)
        tag_value = f.get_tag_value("./MODULES/MODULE/DESCRIPTION1")
        self.assertEqual("",tag_value)



