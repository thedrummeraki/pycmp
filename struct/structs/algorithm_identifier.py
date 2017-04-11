from pyasn1.type.univ import Sequence
from pyasn1.type.univ import Any
from pyasn1.type.univ import ObjectIdentifier
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedTypes


"""
AlgorithmIdentifier ::= SEQUENCE {
	                    algorithm OBJECT IDENTIFIER,
	                    parameters ANY DEFINED BY algorithm OPTIONAL 
					}
"""


class AlgorithmIdentifier(Sequence):
	def __init__(self, algorithm, parameters=None):
		Sequence.__init__(self, componentType=NamedTypes(
			NamedType('algorithm', ObjectIdentifier(value=algorithm)),
			OptionalNamedType('parameters', Any(value=parameters))
		))
