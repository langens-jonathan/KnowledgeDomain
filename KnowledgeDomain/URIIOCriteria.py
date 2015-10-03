__author__ = 'Jonathan Langens'
from URIIO import URIProperty
from Criteria import Criteria
"""
Copyright (C) 2015  Langens Jonathan

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
class URIIOCriteria(Criteria):

    def __init__(self, URIIOList):
        self.URIIOList = URIIOList
        self.URIRestrictions = []
        self.PropertyRestrictions = []
        self.PredicateRestrictions = []
        self.TypeRestrictions = []

    def getCriteriaType(self):
        return "uriioCriteria"

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