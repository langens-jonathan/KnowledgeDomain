__author__ = 'Jonathan Langens'
from URIIO import URIProperty

class URIIOCriteria:

    def __init__(self, URIIOList):
        self.URIIOList = URIIOList
        self.URIRestrictions = []
        self.PropertyRestrictions = []
        self.PredicateRestrictions = []
        self.TypeRestrictions = []

    def addURIRestriction(self, uri):
        self.URIRestrictions.append(uri)

    def addPropertyRestriction(self, name, value):
        self.PropertyRestrictions.append(URIProperty(name, value))

    def addPredicateRestriction(self, subjet, predicate, object):
        #self.PredicateRestrictions.append((URIPredicate(predicate, object)))
        test = 1

    def __URIRestrictionListContains__(self, uri):
        for urii in self.URIRestrictions:
            if uri == urii:
                return True
        return False

    def __passesPropertyRestrictionList__(self, uriio):
        for prop in self.PropertyRestrictions:
            if prop.name == None:
                hasOnePropertyWithValue = False
                for propinurrio in uriio.properties:
                    if propinurrio.value == prop.value:
                        hasOnePropertyWithValue = True
                if hasOnePropertyWithValue == False:
                    return False
            else:
                propinuriio = uriio.getProperty(prop.name)
                if propinuriio == None:
                    return False
                if prop.value != None:
                    if propinuriio.value != prop.value:
                        return False
        return True

    # REWRITE THIS SHOULD CONSIDER THE OBJECT TO BE ANOTHER URIIO!!! AND NOT A TYPE
    def __passesPredicateRestrictionList__(self, uriio):
        for pred in self.PredicateRestrictions:
            if pred.predicate is not None:
                predfound = False
                for upred in uriio.predicates:
                    if upred.predicate == pred.predicate:
                        predfound = True
                if not predfound:
                    return False
            if pred.object is not None:
                objfound = False
                for upred in uriio.predicates:
                    if upred.object == pred.object:
                        objfound = True
                if not objfound:
                    return False
        return True


    def resolve(self):
        toRemove = []

        for uriio in self.URIIOList:
            if not self.__URIRestrictionListContains__(uriio.URI):
                toRemove.append(uriio)

        if len(self.URIRestrictions) == 0:
            toRemove.clear()

        for uriio in toRemove:
            self.URIIOList.remove(uriio)

        toRemove.clear()

        for uriio in self.URIIOList:
            if not self.__passesPropertyRestrictionList__(uriio):
                toRemove.append(uriio)

        for uriio in toRemove:
            self.URIIOList.remove(uriio)

        toRemove.clear()
        """
        for uriio in self.URIIOList:
            if not self.__passesPredicateRestrictionList__(uriio):
                toRemove.append(uriio)
        """
        for uriio in toRemove:
            self.URIIOList.remove(uriio)

        toRemove.clear()

    def getURIIOs(self):
        return self.URIIOList

    def asXML(self):
        toreturn = "<URIIOS>"
        for u in self.URIIOList:
            toreturn += u.asXML()
        toreturn += "</URIIOS>"
        return toreturn