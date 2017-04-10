from pyasn1.codec.ber import decoder as ber_decoder
from pyasn1.codec.cer import decoder as cer_decoder
from pyasn1.codec.der import decoder as der_decoder

from utils import errors


class ASN1Structure:
    def __init__(self, string, enc='der'):
        decoder = None
        if enc == 'der':
            decoder = der_decoder
        elif enc == 'cer':
            decoder = cer_decoder
        elif enc == 'ber':
            decoder = ber_decoder
        else:
            raise errors.EncodingChoiceError(enc)

        try:
            self._res = decoder.decode(string)[0]
        except:
            raise errors.PyCMPError('')

    def to_asn1_struct(self):
        return self._res

    def __str__(self):
        return self._res.prettyPrint()

