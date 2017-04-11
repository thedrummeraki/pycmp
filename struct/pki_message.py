from pyasn1.type.univ import Sequence
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import NamedTypes
from pyasn1.type.namedtype import OptionalNamedType

from pki_header import PKIHeader


"""
PKIMessage ::= SEQUENCE {
         header           PKIHeader,
         body             PKIBody,
         protection   [0] PKIProtection OPTIONAL,
         extraCerts   [1] SEQUENCE SIZE (1..MAX) OF CMPCertificate
                          OPTIONAL
     }
"""

class PKIMessage(Sequence):
    def __init__(self, sender, recipient):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType('header', PKIHeader(pvno=2, sender=sender, recipient=recipient)),
            NamedType('body', None),
            NamedType('protection', None),
            OptionalNamedType('extraCerts', None),
        ))

