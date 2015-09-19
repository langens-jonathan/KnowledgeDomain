__author__ = 'Jonathan Langens'
from URIIOType import  URIIOType
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
. self.atomicProperties = all properties that should be shared by the types, types for which the supertypes have all ato
mic properties will also be accepted
. self.typeProperties = all type properties that should be shared by the types, types for which the supertypes have all
 type properties will also be accepted
"""
class URIIOTypeCriteria:
    def __init__(self, typeList):
        self.typeList = typeList
        self.type = None
        self.atomicProperties = []
        self.typeProperties = []
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

    def __clearBasedOnAtomicProperties__(self):
        list = []
        for tp in self.typeList:
            for ap in self.atomicProperties:
                if not tp.hasAtomicProperty(ap):
                    list.append(tp)
        for tp in list:
            self.typeList.remove(tp)

    def __clearBasedOnTypeProperty__(self):
        list = []
        for tp in self.typeList:
            for ap in self.typeProperties:
                if not tp.hasTypeProperty(ap):
                    list.append(tp)
        for tp in list:
            self.typeList.remove(tp)

    def resolve(self):
        if self.type is not None:
            self.__clearBasedOnType__()
        self.__clearBasedOnAtomicProperties__()
        self.__clearBasedOnTypeProperty__()

    def asXML(self):
        xmlString = "<types>"
        for tp in self.typeList:
            xmlString += "<type>"
            xmlString += "<name>" + tp.type + "</name>"
            parentName = ""
            if tp.parent is not None:
                parentName = tp.parent.type
            xmlString += "<parent>" + parentName + "</parent>"
            xmlString += "<atomicProperties>"
            for ap in tp.atomicProperties:
                xmlString += "<atomicProperty>" + ap + "</atomicProperty>"
            xmlString += "</atomicProperties>"
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
