from pyasn1.type import univ, namedtype, tag, char


def get_implicit_tag(position):
    return tag.Tag(tag.tagClassContext, tag.tagFormatSimple, position)
