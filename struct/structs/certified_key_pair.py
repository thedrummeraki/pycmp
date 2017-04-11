from pyasn1.type.univ import Sequence
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import NamedTypes

from structs.pki_publication_info import PKIPublicationInfo
from structs.encrypted_value import EncryptedValue
from structs.cert_or_enc_cert import CertOrEncCert


class CertifiedKeyPair(Sequence):
    def __init__(self, value, pkey=None, pki_publication_info=None):
        Sequence.__init__(self, componentType=NamedTypes(
            NamedType('certOrEncCert', CertOrEncCert(value)),
            OptionalNamedType('privateKey', EncryptedValue(pkey)),
            OptionalNamedType('publicationInfo', PKIPublicationInfo(pki_publication_info))
        ))
