
class PyCMPError(BaseException):
    def __init__(self, message=None, cause=None):
        self.message = message
        self.cause = cause

    def __str__(self):
        msg = self.message if self.message else 'Unknown %s error' % self.name()
        cas = self.cause if self.cause else 'Cause unknown.'

        return '%s (Cause: %s)' % (msg, cas)

    def name(self):
        return self.__class__.__name__


class EncodingChoiceError(PyCMPError):
    def __init__(self, chosen_enc):
        PyCMPError.__init__(self, 'Invalid encoding.', '%s is not a valid encoding.' % chosen_enc)

