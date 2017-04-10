from pyasn1.type.univ import Sequence
from pyasn1.codec.ber import decoder as ber_decoder
from pyasn1.codec.cer import decoder as cer_decoder
from pyasn1.codec.der import decoder as der_decoder

from utils import errors


class ASN1Sequence(Sequence):
    def __init__(self, string, enc='der'):
        if enc == 'der':
            decoder = der_decoder
        elif enc == 'cer':
            decoder = cer_decoder
        elif enc == 'ber':
            decoder = ber_decoder
        else:
            raise errors.EncodingChoiceError(enc)

        try:
            _res = decoder.decode(string)[0]
        except:
            raise errors.PyCMPError('')

        Sequence.__init__(
            self,
            componentType=_res.componentType,
            tagSet=_res.tagSet,
            subtypeSpec=_res.subtypeSpec,
            sizeSpec=_res.sizeSpec
        )

        if isinstance(_res, Sequence):
            for idx in range(len(_res)):
                component = _res.getComponentByPosition(idx)
                if component:
                    self.setComponentByPosition(idx, value=component)
        else:
            raise errors.PyCMPError('Invalid sequence', 'Expected ASN1 Sequence')

    def __str__(self):
        return self.prettyPrint()

