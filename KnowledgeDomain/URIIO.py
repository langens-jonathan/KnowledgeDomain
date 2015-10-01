__author__ = 'Jonathan Langens'
from KnowledgeDomainDefinitions import KnowledgeDomainDefinitions
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
"""
@classname URIIdentifiedObject
@author Jonathan Langens
@created 17/08/2015
@version 0.01
@description A URI Identified Object is a generic class that describes an object or an idea
             It contains of a URI that identifies this object, and of three lists. A list with
             types (ontae) of which the most definite type is positioned at the last position and
             the most general type (URIIO) is at position 0. A list of properties of type URIProperty
             and a list of predicates of type URIPredicate
"""
class URIIO:

    """
    @param URI the URI that gets passed to the constructor should be unique
    @pre a unique URI has to be passed
    @post the URI_Identified_Object is correctly initialized with a unique URI and with the URIIO type set at ontae[0]
    """
    def __init__(self, URI):
        self.URI = URI
        self.type = []
        self.properties = []

    """
    @param type a type object that is known in the type dictionary of this domain
    @post this URIIO has only 1 type and that is the type passed. we KNOW the URIIO IS of this type.
    """
    def setType(self, type):
        self.type = []
        self.type.append(type)

    """
    @param type a type object that is known in the type dictionary of this domain
    @post the passed type is added to this URIIO's type list, another possibility of this URIIO's type is added
    """
    def addType(self, type):
        self.type.append(type)

    """
    @param name the name of the property (i.e. for car.color we would use "color" for the name)
    @param value the value of the property(i.e. for a red color we would use "red" for the value)
    @post the property is initialized as a URIProperty with name and value
    """
    def addProperty(self, name, value, type = KnowledgeDomainDefinitions.TEXT):
        prop = self.getProperty(name)
        if prop == None:
            self.properties.append(URIProperty(name, value, type))
        else:
            prop.value = value


    """
    @param name the name of the property you wish to retrieve
    @return if this URIIO contains a property with the given name then that property else None
    """
    def getProperty(self, name):
        for p in self.properties:
            if p.name == name:
                return p
        return None

    """
    @param name the name of the property that should be removed
    @post if the property is found it is removed
    """
    def removeProperty(self, name):
        prop = self.getProperty(name)
        if prop is not None:
            self.properties.remove(prop)

    """
    @result the entire URIIO as an XML Object
    """
    def asXML(self):
        toreturn = "<URIIO>"
        toreturn += "<URI>" + self.URI + "</URI>"
        toreturn += "<types>"
        for t in self.type:
            toreturn += "<type>" + t.type + "</type>"
        toreturn += "</types>"
        toreturn += "<properties>"
        for p in self.properties:
            toreturn += "<property><name>" + p.name + "</name>"
            toreturn += "<value>" + str(p.value) + "</value></property>"
        toreturn += "</properties>"
        toreturn += "</URIIO>"
        return toreturn


"""
@classname URI Property
@author Jonathan Langens
@created 17/08/2015
@version 0.01
@description a small helper class that defines a property as 2 strings
"""
class URIProperty:
    def __init__(self, name, value, type = KnowledgeDomainDefinitions.TEXT):
        self.name = name
        self.value = value
        self.type = type
