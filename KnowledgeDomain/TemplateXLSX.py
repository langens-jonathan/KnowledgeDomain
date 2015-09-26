__author__ = 'jeuna'
from Template import Template
class TemplateXLSX(Template):
    def __init__(self):
        return

    def getHashCode(self):
        return "XLSXHash"


"""
@description an XLSXObjectTemplate describes 1 URIIO somewhere in an XLSX file. It will be used to construct a URIIO
    and the predicates that give it meaning in the knowledge domain
"""
class XLSXObjectTemplate:
    def __init__(self, type):
        self.type = type
        self.properties = []
        self.connectors = []


"""
@description an XLSXObjectPropertyTemplate describes a property that will be added to the host URIIO with the name
    found at position namex, namey and value at position x,y (also type at x,y)
"""
class XLSXObjectPropertyTemplate:
    def __init__(self, x, y, namex, namey):
        self.x = x
        self.y = y
        self.namex = namex
        self.namey = namey


"""
@description an XLSX Connector connects the host URIIO to another which might has a certain type, and a property which
    which has the same value that is found at position x,y in the xlsx file. The predicate that connects this to that
    URIIO is given as a string. The result in the predicate library will be:
    <Other URIIO> <predicate> <this URIIO>
    where that other URIIO has the desired type (this can be none) and the property with value at x,y
"""
class XLSXObjectConnectorTemplate:
    def __init__(self, x, y, type, property, predicate, subject):
        self.x = x
        self.y = y
        self.type = type # this is the type on which the property connects
        self.property = property
        self.predicate = predicate
        self.subject = subject