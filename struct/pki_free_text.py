from pyasn1.type.univ import SequenceOf
from pyasn1.type.char import UTF8String


class PKIFreeText(SequenceOf):
    componentType = UTF8String()
