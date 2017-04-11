from pyasn1.type.univ import Sequence
from pyasn1.codec.der import encoder

from OpenSSL import crypto

import sys; sys.path.append("..")
from asn1_struct import ASN1Sequence
from utils.errors import PyCMPError


class Certificate(ASN1Sequence):
    def __init__(self, cert):
        if not isinstance(cert, crypto.X509):
            raise PyCMPError('Invalid certificate', 'Expected OpenSSl.crypto.X509 instance')

        string = crypto.dump_certificate(2, cert)
        ASN1Sequence.__init__(self, string, enc='der')

    def to_x509(self):
        enc = encoder.encode(self)
        return crypto.load_certificate(crypto.FILETYPE_ASN1, enc)


    @staticmethod
    def load_der_file(fop):
        return Certificate.load_file(fop, 2)

    @staticmethod
    def load_pem_file(fop):
        return Certificate.load_file(fop, 1)

    @staticmethod
    def load_file(file_or_path, enc):
        if isinstance(file_or_path, file):
            f = file_or_path
        else:
            f = open(file_or_path)
        with f:
            return Certificate.load_string(f.read(), enc)

    @staticmethod
    def load_der_string(string):
        return Certificate.load_string(string, 2)

    @staticmethod
    def load_pem_string(string):
        return Certificate.load_string(string, 1)

    @staticmethod
    def load_string(string, enc):
        return Certificate(crypto.load_certificate(enc, string))
