from pyasn1.type.univ import Choice
from pyasn1.type.univ import ObjectIdentifier
from pyasn1.type.char import UTF8String
from pyasn1.type.univ import Set
from pyasn1.type.univ import Sequence
from pyasn1.type.tag import Tag
from pyasn1.type.tag import TagSet
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import NamedTypes
from pyasn1.type.namedtype import OptionalNamedType

from pyasn1.type import univ, namedtype, tag, char

from utils import utils


"""
GeneralName ::= CHOICE {
      otherName                       [0]     OtherName,
      rfc822Name                      [1]     IA5String,
      dNSName                         [2]     IA5String,
      x400Address                     [3]     ORAddress,
      directoryName                   [4]     Name,
      ediPartyName                    [5]     EDIPartyName,
      uniformResourceIdentifier       [6]     IA5String,
      iPAddress                       [7]     OCTET STRING,
      registeredID                    [8]     OBJECT IDENTIFIER}

 OtherName ::= SEQUENCE {
      type-id    OBJECT IDENTIFIER,
      value      [0] EXPLICIT ANY DEFINED BY type-id }

 EDIPartyName ::= SEQUENCE {
      nameAssigner            [0]     DirectoryString OPTIONAL,
      partyName               [1]     DirectoryString }

 Name ::= CHOICE { RDNSequence }
"""


DN_OID = {
    'C': '2.5.4.6',
    'CN': '2.5.4.3',
    'L': '2.5.4.7',
    'ST': '2.5.4.8',
    'O': '2.5.4.10',
    'OU': '2.5.4.11'
}


class GeneralName(Sequence):
    def __init__(self, x509_name):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType(DN())
        ))


class DN(Set):
    def __init__(self, dn=None, value=None):
        self._set_dn = True if dn is not None else False
        self._dn = None
        Set.__init__(self, componentType=NamedTypes(
            NamedType('nest', Sequence(componentType=NamedTypes(
                NamedType('oid', ObjectIdentifier()),
                NamedType('string', UTF8String())
            )))
        ), tagSet=TagSet((), Tag(tagClass=0, tagFormat=32, tagId=17)))

        self.set_dn(dn)
        self.set_value(value)

    def set_dn(self, dn):
        if dn is None:
            return
        if dn not in DN_OID.keys():
            raise Exception('Non-supported DN %s' % dn)

        seq = self.getComponentByPosition(0)
        seq.setComponentByName('oid', ObjectIdentifier(DN_OID[dn]))
        self._set_dn = True

    def set_value(self, value):
        if value is None:
            return
        if not self._set_dn:
            raise Exception('Please set the DN (one of %s)' % str(DN_OID.keys()))
        seq = self.getComponentByPosition(0)
        seq.setComponentByName('string', UTF8String(value))

    def get_value(self):
        if not self._set_dn:
            return None
        seq = self.getComponentByPosition(0)
        return seq.getComponentByName('string')

    def __str__(self):
        if not isinstance(self._dn, str) or not self._set_dn:
            return "[DN: <unset>]"
        return '[DN: %s=%s]' % (self._dn.upper(), self.get_value())


class OtherName:
    def __init__(self):
        self._asn1_struct = Sequence()

    def to_asn1_struct(self):
        return self._asn1_struct

    def get_type_id(self):
        pass

    def get_value(self):
        pass


class EDIPartyName(Sequence):
    def __init__(self, value):
        Sequence.__init__(self, componentType=NamedTypes(
        ))

    def get_party_name(self):
        pass

    def get_name_assigner(self):
        pass

