from pyasn1.type.univ import Sequence
from pyasn1.type.univ import Integer
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedTypes
from pyasn1.type.univ import OctetString

from pki_status_info import PKIStatusInfo


class CertResponse(Sequence):

    def __init__(self, status, cert_req_id, resp_info=None, cert=None):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType('certReqId', Integer(cert_req_id)),
            NamedType('status', PKIStatusInfo(status)),
            NamedType('rspInfo', OctetString(value=resp_info)),
            NamedType('')
        ))
