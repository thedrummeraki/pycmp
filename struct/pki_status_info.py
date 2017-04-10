from pyasn1.type.univ import Sequence
from pyasn1.type.namedtype import NamedTypes
from pyasn1.type.namedtype import NamedType

from pki_status import PKIStatus
from pki_free_text import PKIFreeText
from pki_failure_info import PKIFailureInfo


class PKIStatusInfo(Sequence):

    def __init__(self, status, free_text=None, fail_info=None):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType('status', PKIStatus(value=status)),
            NamedType('statusString', PKIFreeText()),
            NamedType('failInfo', PKIFailureInfo(value=fail_info))
        ))
