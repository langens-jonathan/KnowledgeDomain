__author__ = 'Jonathan Langens'

from URIIO import URIIO
from URIIOCriteria import URIIOCriteria

"""
@classname URIManager
@author Jonathan Langens
@created 18/08/2015
@version 0.01
@description A container class that contains a list of URI Identified Objects and some functionality to manipulate
them.
"""

class URIIOManager:

    """
    @param domain the name of this domain, this also serves as prefix for the URI's of all URIIOs in this domain
    @pre the domain name passed should be unique
    @post the domain initializes the URIIO list and sets its URI counter to 0
    """
    def __init__(self, domain):
        self.domain = domain
        self.uricounter = 0
        self.URIIOs = []

    """
    """
    def getURIIO(self, uri):
        for u in self.URIIOs:
            if u.URI == uri:
                return u
        return None

    def removeURIIO(self, uri):
        for u in self.URIIOs:
            if u.URI == uri:
                self.URIIOs.remove(u)
                return

    """
    @description This function returns a new URIIO instance that then can be modified to represent what it should. The U
    RIIO is also added to this domains list of URIIO's. This function is the only way to add URIIO's to this domain.
    """
    def newURIIO(self):
        uriio = URIIO(self.__nextURI__())
        self.URIIOs.append(uriio)
        return uriio

    """
    @accesibility private
    @description returns a valid URI for this domain
    """
    def __nextURI__(self):
        uri = self.domain + "/" + str(self.uricounter)
        self.uricounter += 1
        return uri

    """
    @description returns a new criteria object that is instantiated to contain all objects that are part of the current
    world
    """
    def getCriteria(self):
        ulist = []
        for u in self.URIIOs:
            ulist.append(u)
        return URIIOCriteria(ulist)


    """
    @description helper function that quickly prints all URIIO's in this manager to the terminal
    """
    def printURIIOManager(self):
        tl = self.asPredicateList()
        for t in tl:
            t.printTriple()
