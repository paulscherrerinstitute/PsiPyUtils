##############################################################################
#  Copyright (c) 2018 by Paul Scherrer Institute, Switzerland
#  All rights reserved.
#  Authors: Oliver Bruendler
##############################################################################

import re

class TagsNotFoundError(Exception): pass

def TaggedReplace(startTag : str, endTag : str, text : str, file : str):
    """
    Replace the text between two tags in a file with a different text. This is very useful for code generation and
    modification.

    Example:
        1. Assume the following content in a file myText.txt: "bla <st> any text <et> blubb"
        2. Call TaggedReplace("<st>", "<et>", " rabbit ", "myText.txt")
        3. The content of myText.txt after the call will be: "bla <st> rabbit <et> blubb"

    :param startTag: Start tag (the tag itself is not removed)
    :param endTag: End tag (the tag itself is not removed)
    :param text: Text to put between the tags specified
    :param file: File to do the replacement in
    """
    #Setup
    TAG_REGEX = "{}.*{}".format(startTag, endTag)

    #Open File
    with open(file) as f:
        content = f.read()

    #Check if tags are present
    if not re.search(TAG_REGEX, content, flags=re.DOTALL):
        raise TagsNotFoundError("Tags {} {} are not found in the file {}".format(startTag, endTag, file))

    #Do substitution
    content = re.sub(TAG_REGEX, "{}{}{}".format(startTag, text, endTag), content, flags=re.DOTALL)
    with open(file, "w+") as f:
        f.write(content)

