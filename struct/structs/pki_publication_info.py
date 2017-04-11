from pyasn1.type.univ import Integer
from pyasn1.type.univ import Sequence
from pyasn1.type.univ import SequenceOf
from pyasn1.type.namedval import NamedValues
from pyasn1.type.namedtype import OptionalNamedType
from pyasn1.type.namedtype import NamedType
from pyasn1.type.namedtype import NamedTypes


class SinglePubInfo(Sequence):
	def __init__(self, value, pub_location=None):
		Sequence.__init__(self, componentType=NamedTypes(
			NamedType('pubMethod', Integer(value=value, namedValues=NamedValues(
				('dontCare', 0),
				('x500', 1),
				('web', 2),
				('ldap', 3)
			))),
			OptionalNamedType('pubLocation', GeneralName(value=pub_location))
		))


class PKIPublicationInfo(Sequence):
	def __init__(self, value):
		Sequence.__init__(self, componentType=NamedTypes(
			NamedType('action', Integer(value=value)),
			NamedType('pubInfos', SequenceOf(componentType=SinglePubInfo()))
		))
