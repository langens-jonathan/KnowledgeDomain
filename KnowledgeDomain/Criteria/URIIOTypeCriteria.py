__author__ = 'Jonathan Langens'
from KnowledgeDomain.Type.URIIOType import URIIOType
from KnowledgeDomain.Type.URIIOType import URIIOTypeProperty
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
@classname URIIOTypeCriteria
@author Jonathan Langens
@created 18/08/2015
@version 0.01
@description a URIIOTypeCriteria object helps to query the types of a URIIOTypeManager. It allows to set conditions and
returns all types that conform to those condiditons. Programs that use URIIOTypeCriteria can use the following parameters
. self.type = the name the wanted type is to have
. self.properties = all properties that should be shared by the types, types for which the supertypes have all properties will also be accepted
. self.propertyTypes = all URIIOTypes that have at least one property of those types are added
"""
class URIIOTypeCriteria:
    def __init__(self, typeList):
        self.typeList = typeList
        self.type = None
        self.properties = []
        self.propertyTypes = []
        self.exactType = False

    def __clearBasedOnType__(self):
        list = []
        for tp in self.typeList:
            if not self.exactType:
                if not tp.isOfType(self.type.type):
                    list.append(tp)
            else:
                if not tp.type == self.type.type:
                    list.append(tp)
        for tp in list:
            self.typeList.remove(tp)

    def __clearBasedOnProperties__(self):
        list = []
        for tp in self.typeList:
            for ap in self.properties:
                if not tp.hasAtomicProperty(ap):
                    list.append(tp)
        for tp in list:
            self.typeList.remove(tp)

    def __clearBasedOnPropertyTypes__(self):
        list = []
        for ut in self.typeList:
            utsbr = False
            for tp in self.propertyTypes:
                for p in ut.properties:
                    if not p.type == tp:
                        utsbr = True
            if utsbr:
                list.append(ut)

        for tp in list:
            self.typeList.remove(tp)

    def resolve(self):
        if self.type is not None:
            self.__clearBasedOnType__()
        self.__clearBasedOnProperties__()
        self.__clearBasedOnPropertyTypes__()

    def asXML(self):
        xmlString = "<types>"
        for tp in self.typeList:
            xmlString += "<type>"
            xmlString += "<name>" + tp.type + "</name>"
            parentName = ""
            if tp.parent is not None:
                parentName = tp.parent.type
            xmlString += "<parent>" + parentName + "</parent>"
            xmlString += "<properties>"
            for ap in tp.properties:
                xmlString += "<property>" + ap.name + "<type>" + ap.type + "</type></property>"
            xmlString += "</properties>"
            lockedString = "0"
            if tp.locked:
                lockedString = "1"
            xmlString += "<locked>" + lockedString + "</locked>"
            sysDefString = "0"
            if tp.systemDefined:
                sysDefString = "1"
            xmlString += "<systemDefined>" + sysDefString + "</systemDefined>"
	    xmlString += "<children>"
	    for ch in tp.children:
		xmlString += "<child>" + ch.type + "</child>"
	    xmlString += "</children>"
            xmlString += "</type>"
        xmlString += "</types>"
        return xmlString
