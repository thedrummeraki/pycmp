from pyasn1.type.univ import BitString
from pyasn1.type.univ import OctetString
from pyasn1.type.univ import Sequence
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedTypes

from algorithm_identifier import AlgorithmIdentifier
from utils import utils


"""
 EncryptedValue ::= SEQUENCE {
                     intendedAlg   [0] AlgorithmIdentifier  OPTIONAL,
                     -- the intended algorithm for which the value will be used
                     symmAlg       [1] AlgorithmIdentifier  OPTIONAL,
                     -- the symmetric algorithm used to encrypt the value
                     encSymmKey    [2] BIT STRING           OPTIONAL,
                     -- the (encrypted) symmetric key used to encrypt the value
                     keyAlg        [3] AlgorithmIdentifier  OPTIONAL,
                     -- algorithm used to encrypt the symmetric key
                     valueHint     [4] OCTET STRING         OPTIONAL,
                     -- a brief description or identifier of the encValue content
                     -- (may be meaningful only to the sending entity, and used only
                     -- if EncryptedValue might be re-examined by the sending entity
                     -- in the future)
                     encValue       BIT STRING }
                     -- the encrypted value itself
"""

class EncryptedValue(Sequence):
	def __init__(self, enc_value, intended_alg=None, symm_alg=None, enc_symm_key=None, key_alg=None, value_hint=None):
		Sequence.__init__(self, componentType=NamedTypes(
			OptionalNamedType('encValue', BitString(value=enc_value)),
			OptionalNamedType('intentedAlg', AlgorithmIdentifier(value=intended_alg).subtype(implicitTag=utils.get_implicit_tag(0))),
			OptionalNamedType('symmAlg', AlgorithmIdentifier(value=symm_alg).subtype(implicitTag=utils.get_implicit_tag(1))),
			OptionalNamedType('encSymmKey', BitString(value=enc_symm_key).subtype(implicitTag=utils.get_implicit_tag(2))),
			OptionalNamedType('keyAlg', AlgorithmIdentifier(value=key_alg).subtype(implicitTag=utils.get_implicit_tag(3))),
			OptionalNamedType('valueHint', OctetString(value=value_hint).subtype(implicitTag=utils.get_implicit_tag(4)))
		))
