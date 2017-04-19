from pyasn1.type.univ import Sequence
from pyasn1.type.univ import SequenceOf
from pyasn1.type.univ import Integer
from pyasn1.type.univ import OctetString

from pyasn1.type.namedtype import NamedTypes
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import OptionalNamedType

from pyasn1.type.tag import Tag
from pyasn1.type.tag import TagSet

from pyasn1.type.useful import GeneralizedTime


from structs.general_name import GeneralName
from structs.algorithm_identifier import AlgorithmIdentifier
from structs.key_identifier import KeyIdentifier
from pki_free_text import PKIFreeText

"""
ASN1 Structure:
PKIHeader ::= SEQUENCE {
         pvno                INTEGER     { cmp1999(1), cmp2000(2) },
         sender              GeneralName,
         recipient           GeneralName,
         messageTime     [0] GeneralizedTime         OPTIONAL,
         protectionAlg   [1] AlgorithmIdentifier     OPTIONAL,
         senderKID       [2] KeyIdentifier           OPTIONAL,
         recipKID        [3] KeyIdentifier           OPTIONAL,
         transactionID   [4] OCTET STRING            OPTIONAL,
         senderNonce     [5] OCTET STRING            OPTIONAL,
         recipNonce      [6] OCTET STRING            OPTIONAL,
         freeText        [7] PKIFreeText             OPTIONAL,
         generalInfo     [8] SEQUENCE SIZE (1..MAX) OF
                             InfoTypeAndValue     OPTIONAL
     }
     PKIFreeText ::= SEQUENCE SIZE (1..MAX) OF UTF8String
"""


class PKIHeader(Sequence):
    def __init__(self):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType('pvno', Integer()),
            NamedType('sender', GeneralName()),
            NamedType('recipient', GeneralName()),
            NamedType('messageTime', GeneralizedTime()),
            NamedType('protectionAlg', AlgorithmIdentifier()),
            NamedType('senderKID', OctetString()),
            NamedType('recipKID', OctetString()),
            NamedType('transactionID', OctetString())
        ), tagSet=TagSet((), Tag(tagClass=0, tagFormat=32, tagId=16)))
