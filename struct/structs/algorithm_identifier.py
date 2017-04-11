from pyasn1.type.univ import Sequence
from pyasn1.type.univ import Any
from pyasn1.type.univ import ObjectIdentifier
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedTypes


"""
AlgorithmIdentifier ::= SEQUENCE {
                        algorithm OBJECT IDENTIFIER,
                        parameters ANY DEFINED BY algorithm OPTIONAL 
                    }
"""


class AlgorithmIdentifier(Sequence):
    def __init__(self, value, parameters=None, tagSet=None, subtypeSpec=None, sizeSpec=None):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType('algorithm', ObjectIdentifier(value=value)),
        ), tagSet=tagSet, subtypeSpec=subtypeSpec, sizeSpec=sizeSpec)


if __name__ == '__main__':

    from pyasn1.type import tag
    def get_implicit_tag(position):
        return tag.Tag(tag.tagClassContext, tag.tagFormatSimple, position)

    value = '2.1.1.1.1.2'
    params = None

    a = AlgorithmIdentifier(value=value, parameters=params)
    print '----'
    print a.subtype(implicitTag=get_implicit_tag(1))
