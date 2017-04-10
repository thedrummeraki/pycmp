# pycmp

A Python implementation of Certificate Management Protocol (as known as CMP) data structures.
The implementation of this project will follow [RFC #4210](https://www.ietf.org/rfc/rfc4210.txt).

Here is a list of different data structures to be coverted. Any contrubition is welcome!

- PKIMessage
- PKIHeader
- PKIFreeText
- PKIBody
- PKIProtection
- ProtectedPart
- PBMParameter
- DHBMParameter
- NestedMessageContent
- PKIStatus
- PKIFailureInfo
- PKIStatusInfo
- OOBCertHash
- POPOSigningKeyInput
- POPODecKeyChallContent
- Challenge
- POPODecKeyRespContent
- CertReqMessage
- CertResponse
- CertifiedKeyPair
- CertOrEncCert
- KeyRecReqContent
- RevReqContent
- RevDetails
- RevRepContent
- CAKeyUpdAnnContent
- CertAnnContent
- RevAnnContent
- CRLAnnContent
- PKIConfirmContent
- CertConfirmContent
- CertStatus
- InfoTypeAndValue
- GenMsgContent
- ErrorMsgContent
- PollReqContent

Should some of the data structures defined above become unnecessary, they will be removed accordingly.
This is a very new project, and is therefore not useable. But please feel free to check it out and make changes as you see fit.

Dependencies:
- [pyOpenSSL] (http://www.pyopenssl.org/en/stable/)
- [pyasn1] (http://pyasn1.sourceforge.net/)

