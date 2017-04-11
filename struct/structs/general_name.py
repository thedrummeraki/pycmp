from pyasn1.type.univ import Choice
from pyasn1.type.univ import Sequence
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


class GeneralName(Choice):
    def __init__(self, value):
        Choice.__init__(self, componentType=NamedTypes(
            OptionalNamedType('otherName', char.IA5String(value=value).subtype(implicitTag=utils.get_implicit_tag(0))),
            OptionalNamedType('rfc822Name', char.IA5String(value=value).subtype(implicitTag=utils.get_implicit_tag(1))),
            # OptionalNamedType('ediPartyName', EDIPartyName(value=value).subtype(implicitTag=utils.get_implicit_tag(5))),
            OptionalNamedType('uniformResourceIdentifier', char.IA5String(value=value).subtype(implicitTag=utils.get_implicit_tag(6))),
            OptionalNamedType('iPAddress', univ.OctetString(value=value).subtype(implicitTag=utils.get_implicit_tag(7))),
            OptionalNamedType('registeredID', univ.ObjectIdentifier(value=value).subtype(implicitTag=utils.get_implicit_tag(8))),
        ))

    def get_other_name(self):
        pass

    def get_rfc822_name(self):
        pass

    def get_dns_name(self):
        pass

    def get_x400_address(self):
        pass

    def get_directory_name(self):
        pass

    def edi_party_name(self):
        pass

    def get_uniform_resource_identifier(self):
        pass

    def get_ip_address(self):
        pass

    def get_registered_id(self):
        pass


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

