from pyasn1.type.univ import Integer
from pyasn1.type.namedval import NamedValues

"""
PKIStatus ::= INTEGER {
            accepted               (0),
            grantedWithMods        (1),
            rejection              (2),
            waiting                (3),
            revocationWarning      (4),
            revocationNotification (5),
            keyUpdateWarning       (6)
        }
"""


class PKIStatus(Integer):
    namedValues = NamedValues(
        ('accepted', 0),
        ('grantedWithMods', 1),
        ('rejection', 2),
        ('waiting', 3),
        ('revocationWarning', 4),
        ('revocationNotification', 5),
        ('keyUpdateWarning', 6)
    )

    def __init__(self, value, tagSet=None, subtypeSpec=None, namedValues=None):
        Integer.__init__(self, value=value, tagSet=tagSet, subtypeSpec=subtypeSpec, namedValues=namedValues)


