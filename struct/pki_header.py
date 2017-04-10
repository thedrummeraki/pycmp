

"""
ASN1 Structure:
PKIHeader ::= SEQUENCE {
         pvno                INTEGER     { cmp1999(1), cmp2000(2) },
         sender              GeneralName,
         recipient           GeneralName,
         messageTime     [0] GeneralizedTime         OPTIONAL,
         protectionAlg   [1] AlgorithmIdentifier     OPTIONAL,
         senderKID       [2] KeyIdentifier           OPTIONAL,
         recipKID        [3] KeyIdentifier           OPTIONAL,
         transactionID   [4] OCTET STRING            OPTIONAL,
         senderNonce     [5] OCTET STRING            OPTIONAL,
         recipNonce      [6] OCTET STRING            OPTIONAL,
         freeText        [7] PKIFreeText             OPTIONAL,
         generalInfo     [8] SEQUENCE SIZE (1..MAX) OF
                             InfoTypeAndValue     OPTIONAL
     }
     PKIFreeText ::= SEQUENCE SIZE (1..MAX) OF UTF8String
"""


class PKIHeader():
    def __init__(self, pvno, sender, recipient):
        self._sender = sender
        self._recipient = recipient
        self._pvno = pvno

    def get_pvno(self):
        return self._pvno

    def get_sender(self):
        return self._sender

    def get_recipient(self):
        return self._recipient

    def get_message_time(self):
        pass

    def get_protection_alg(self):
        pass

    def get_sender_kid(self):
        pass

    def get_recip_kid(self):
        pass

    def get_transaction_id(self):
        pass

    def get_sender_nonce(self):
        pass

    def get_recip_nonce(self):
        pass

    def get_free_text(self):
        pass

    def get_general_info(selfish):
        pass
