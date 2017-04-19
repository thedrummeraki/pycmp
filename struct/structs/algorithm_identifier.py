from pyasn1.type.univ import Sequence
from pyasn1.type.univ import OctetString
from pyasn1.type.univ import Any
from pyasn1.type.univ import ObjectIdentifier
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedTypes

from pyasn1.type.tag import Tag
from pyasn1.type.tag import TagSet


"""
AlgorithmIdentifier ::= SEQUENCE {
                        algorithm OBJECT IDENTIFIER,
                        parameters ANY DEFINED BY algorithm OPTIONAL 
                    }
"""


class AlgorithmIdentifier(Sequence):
    # def __init__(self, value, parameters=None, tagSet=None, subtypeSpec=None, sizeSpec=None):
    #     Sequence.__init__(self, componentType=NamedTypes(
    #         NamedType('algorithm', ObjectIdentifier(value=value)),
    #     ), tagSet=tagSet, subtypeSpec=subtypeSpec, sizeSpec=sizeSpec)

    def __init__(self, value=None):
        Sequence.__init__(
            self,
            componentType=NamedTypes(
                NamedType('algorithm', ObjectIdentifier()),
                OptionalNamedType('parameters', Any(tagSet=TagSet((), Tag(tagClass=0, tagFormat=0, tagId=5))))
            ),
            tagSet=TagSet(
                (),
                Tag(tagClass=0, tagFormat=32, tagId=16),
                Tag(tagClass=128, tagFormat=32, tagId=1)
            )
        )
        if value:
            if isinstance(value, str):
                value = ObjectIdentifier(value)
            if not isinstance(value, ObjectIdentifier):
                raise Exception('Excepted an object identifier string or instance')
            self.set_oid(value)

    def set_oid(self, oid):
        self.setComponentByName('algorithm', ObjectIdentifier(oid))

    def get_oid(self):
        return self.getComponentByName('algorithm')

    def set_params(self, params):
        if not isinstance(params, OctetString):
            params = Any(value=params, tagSet=TagSet((), Tag(tagClass=0, tagFormat=0, tagId=5)))
        self.setComponentByName('parameters', params)


if __name__ == '__main__':

    # from pyasn1.type import tag
    # def get_implicit_tag(position):
    #     return tag.Tag(tag.tagClassContext, tag.tagFormatSimple, position)

    value = '2.1.1.1.1.2'
    # params = None

    a = AlgorithmIdentifier(value)
    print len(a)
    # print a.get_oid()
    # print a
    # a = AlgorithmIdentifier()
    # print a
    # print a.get_oid()
    # a.set_oid(value)
    # print a.get_oid()
    # a.set_oid('1.2.840.113549.1.1.5')
    # print a.get_oid()
    # a.set_params(1)
    # print a


    from structs.general_name import DN
    # dn = DN(dn='C', value='Canada')
    dn = DN()
    print dn.getComponentByName('nest')


    # print '----'
    # print a.subtype(implicitTag=get_implicit_tag(1))
