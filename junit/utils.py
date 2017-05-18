import re
import sys

try:
    unichr                      # python2
except NameError:
    unichr = chr                # python3


# taken from https://github.com/kyrus/python-junit-xml/blob/master/junit_xml/__init__.py
def forceUnicode(var, encoding=None):
    """If not already unicode, decode it"""
    if sys.version_info < (3,0):
        if isinstance(var, unicode):
            ret = var
        elif isinstance(var, str):
            if encoding:
                ret = var.decode(encoding)
            else:
                ret = unicode(var)
        else:
            ret = unicode(var)
    else:
        ret = str(var)

    return ret


# taken from https://github.com/kyrus/python-junit-xml/blob/master/junit_xml/__init__.py
def cleanIllegalXmlChars(stringToClean):
    """Removes any illegal unicode characters from the given XML string"""

    illegalUnichrRanges = [
        (0x00, 0x08),
        (0x0B, 0x1F),
        (0x7F, 0x84),
        (0x86, 0x9F),
        (0xD800, 0xDFFF),
        (0xFDD0, 0xFDDF),
        (0xFFFE, 0xFFFF),
        (0x1FFFE, 0x1FFFF),
        (0x2FFFE, 0x2FFFF),
        (0x3FFFE, 0x3FFFF),
        (0x4FFFE, 0x4FFFF),
        (0x5FFFE, 0x5FFFF),
        (0x6FFFE, 0x6FFFF),
        (0x7FFFE, 0x7FFFF),
        (0x8FFFE, 0x8FFFF),
        (0x9FFFE, 0x9FFFF),
        (0xAFFFE, 0xAFFFF),
        (0xBFFFE, 0xBFFFF),
        (0xCFFFE, 0xCFFFF),
        (0xDFFFE, 0xDFFFF),
        (0xEFFFE, 0xEFFFF),
        (0xFFFFE, 0xFFFFF),
        (0x10FFFE, 0x10FFFF),
    ]
    illegalRanges = ["%s-%s" % (unichr(low), unichr(high))
                     for (low, high) in illegalUnichrRanges
                     if low < sys.maxunicode]
    illegalXmlRegex = re.compile(u'[%s]' % u''.join(illegalRanges))

    return illegalXmlRegex.sub('', stringToClean)
