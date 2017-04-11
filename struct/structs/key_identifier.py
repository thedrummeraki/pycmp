from pyasn1.type.univ import OctetString

"""
KeyIdentifier ::= OCTET STRING
"""


class KeyIdentifier(OctetString):
	def __init__(self, value=None):
		OctetString.__init__(self, value=value)
