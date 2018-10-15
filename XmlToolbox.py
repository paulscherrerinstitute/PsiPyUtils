##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Waldemar Koprek
##############################################################################

import os
import xml.etree.ElementTree as ET

class XmlToolbox:
  """
  A class of toolbox functions for reading and manipulating data in an XML file

  """

  def __init__(self, fileName: str):
    """
    Constructor

    :param fileName: Name of the XML file. The file must exists
    """
    if not os.path.exists(fileName):
      raise FileExistsError("File {} does not exist".format(fileName))
    self._tree = ET.parse(fileName)

  def get_attr_value_by_other_attr(self, tag_path: str, attr_search_name: str, attr_search_value: str, attr_get_name: str):
    """
    Searches for a tag with given path and and given attribute name and value, and
    returns a value of another attribute

    :param tag_path: Path to the tag in a form of "./level1_tag/level2_tag/"
    :type tag_path: str
    :param attr_search_name: Name of the attribute to be checked
    :type attr_search_name: str
    :param attr_search_value: Value of the checked attribute
    :type attr_search_value: str
    :param attr_get_name: Name of the attribute for which the value is returned
    :type attr_get_name: str
    :return: Value of the get attribute
    :rtype: str
    """

    # The format of search string is "./MODULES/MODULE/[@IPTYPE='PROCESSOR']"
    searchstr = tag_path+"[@"+attr_search_name+"='"+attr_search_value+"']"
    e = self._tree.find(searchstr)
    if e is None:
      return ""
    return e.attrib[attr_get_name]

  def get_attr_value(self, tag_path: str, attr_search_name: str):
    """
    Searches for a tag with given attribute name and returns the attribute value

    :param tag_path: Path to the tag in a form of "./level1_tag/level2_tag/"
    :type tag_path: str
    :param attr_search_name: Name of the attribute to be checked
    :type attr_search_name: str
    :return: Value of the attribute
    :rtype: str
    """

    # The format of search string is "./MODULES/MODULE/[@IPTYPE='PROCESSOR']"
    searchstr = tag_path+"[@"+attr_search_name+"='"+attr_search_value+"']"
    e = self._tree.find(searchstr)
    if e is None:
      return ""
    return e.attrib[attr_get_name]

  def get_tag_value(self, tag_path: str):
    """
    Searches for a tag with given path and returns value of that tag

    :param tag_path: Path to the tag in a form of "./level1_tag/level2_tag/"
    :type tag_path: str
    :return: Value of the tag
    :rtype: str
    """
    e = self._tree.find(tag_path)
    if e is None:
      return ""
    return e.text

