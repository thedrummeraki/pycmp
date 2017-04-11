from pyasn1.type.univ import Choice
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import NamedTypes

from pki.certificate import Certificate
from utils import errors


class CertOrEncCert(Choice):
    def __init__(self, cert=None, enc_cert=None):
        if (enc_cert and cert) or (enc_cert and not cert):
            raise errors.PyCMPError('Encrypted certificates are not supported yet.')

        Choice.__init__(self, componentType=NamedTypes(
            NamedType('certificate', Certificate(cert))
        ))
