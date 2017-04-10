from pyasn1.type.univ import BitString
from pyasn1.type.namedval import NamedValues


class PKIFailureInfo(BitString):
    namedValues = NamedValues(
        ('badAlg', 0),
        ('badMessageCheck', 1),
        ('badRequest', 2),
        ('badTime', 3),
        ('badCertId', 4),
        ('badDataFormat', 5),
        ('wrongAuthority', 6),
        ('incorrectData', 7),
        ('missingTimeStamp', 8),
        ('badPOP', 9),
        ('certRevoked', 10),
        ('certConfirmed', 11),
        ('wrongIntegrity', 12),
        ('badRecipientNonce', 13),
        ('timeNotAvailable', 14),
        ('unacceptedPolicy', 15),
        ('unacceptedExtension', 16),
        ('addInfoNotAvailable', 17),
    )

    def __int__(self, value, tagSet=None, subtypeSpec=None, namedValues=None):
        BitString.__init__(
            self,
            value=value,
            tagSet=tagSet,
            subtypeSpec=subtypeSpec,
            namedValues=namedValues
        )


