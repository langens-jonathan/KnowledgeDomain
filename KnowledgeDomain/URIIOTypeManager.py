__author__ = 'Jonathan Langens'
from URIIOType import URIIOType
from URIIOTypeCriteria import URIIOTypeCriteria
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
@classname URIIOTypeManager
@author Jonathan Langens
@created 18/08/2015
@version 0.01
@description the URIIOTypeManager initialises itself with basic types and offers basic functionality to manipulate these
URIIOTypes
"""
class URIIOTypeManager:
    """
    @post a typemanager with a type dictionary that has been properly initialized and filled with basic types
    """
    def __init__(self,):
        self.typeDictionary = self.__buildTypeDictionary__()

    """
    @param type the name of the type you want to obtain
    @return if a type with the passed name exists in the dictionary it is extracted and passed otherwise it returens None
    """
    def getType(self, type):
        if type in self.typeDictionary:
            return self.typeDictionary[type]
        else:
            return None

    """
    @description purge obtains the basic type and uses this to purge all types for more info on purging see URIIOType
    """
    def purgeDictionary(self):
        self.getType("type").purge()

    """
    @param type the name of the type that needs to be evolved for more info on evolving see URIIOType
    @post and evolve type is added to the dictionary and the type tree
    """
    def evolve(self, type):
        etype = self.getType(type).evolve()
        self.typeDictionary[etype.type] = etype

    """
    @param type the name of the type that needs to be deleted
    @pre the type is required not to be a system defined type and to have no children
    @post the type is deleted from the dictionary and the type tree
    """
    def delete(self, type):
        etype = self.getType(type)
        if etype.systemDefined:
            return
        if len(etype.children) == 0:
            if type in self.typeDictionary:
                del self.typeDictionary[type]
                etype.parent.children.remove(etype)

    """
    @param parent the type that is desired to be the parent of the new type
    @paran name the name the new type is to have
    @pre the name has to be unique to the type dictionary/tree
    @post a new type is added to the type tree and to the dictionary
    @return the new type
    """
    def getNewURIIOType(self, parent, name):
        nType = URIIOType(parent, name)
        self.typeDictionary[name] = nType
        return nType

    """
    @param type the name of the type
    @param newParent the name of the type that should be the new parent
    @post if both types exist in the type dictionary then the type is set to have the new parent as its paren
    """
    def switchParents(self, type, newParent):
        etype = self.getType(type)
        if etype is None:
            return
        etype.parent.children.remove(etype)
        enewParent = self.getType(newParent)
        if enewParent is None:
            return
        enewParent.children.append(etype)
        etype.parent = enewParent

    """
    @param type a fully initialized URIIOType that needs to be saved
    @post if type.type exists in the typeDictionary we alter it so it fits the passed type desription
          otherwise we create a new type
    @return the altered or new type
    """
    def saveType(self, type):
        if type.type in self.typeDictionary:
            # the type already exists so we retrieve it
            inDictType = self.getType(type.type)
            # then we reset its type properties and fill them again from the to save type
            inDictType.typeProperties = []
            for tp in type.typeProperties:
                inDictType.typeProperties.append(tp)
            # next reset the atomic properties
            inDictType.atomicProperties = []
            for ap in type.atomicProperties:
                inDictType.atomicProperties.append(ap)
            # then we set the locked flag
            inDictType.locked = type.locked
            # lastly we switch the parent
            if not type.parent == inDictType.parent:
                if type.parent is not None:
                    self.switchParents(inDictType.type, type.parent.type)
            return inDictType
        elif type.parent is None:
            return "<failed>The entered type description did not provide an acceptable parent type.</failed>"
        else:
            nType = self.getNewURIIOType(type.parent, type.type)
            for tp in type.typeProperties:
                nType.typeProperties.append(tp)
            for ap in type.atomicProperties:
                nType.atomicProperties.append(ap)
            nType.locked = type.locked

            return nType



    """
    @description returns a criteria list that is query-able by the criteria class
    """
    def getCriteria(self):
        cTypeList = []

        for k in self.typeDictionary.keys():
            cTypeList.append(self.getType(k))


        return URIIOTypeCriteria(cTypeList)

    """
    @description initializes a dictionary with basic types
    @publicity private
    """
    def __buildTypeDictionary__(self):
        dic = dict()

        type = URIIOType(None, "type")
        type.locked = True
        type.systemDefined = True
        dic["type"] = type

        idea = URIIOType(type,"idea")
        idea.locked = True
        idea.systemDefined = True
        dic["idea"] = idea

        obj = URIIOType(type, "object")
        obj.locked = True
        obj.systemDefined = True
        dic["object"] = obj

        dataSource = URIIOType(obj, "datasource")
        dataSource.atomicProperties.append("location")
        dic["datasource"] = dataSource
        datastore = URIIOType(dataSource, "datastore")
        dic["datastore"] = datastore
        link = URIIOType(dataSource, "link")
        dic["link"] = link

        person = URIIOType(obj, "person")
        dic["person"] = person
        person.atomicProperties.append("first name")
        person.atomicProperties.append("last name")
        person.atomicProperties.append("date of birth")

        employee = URIIOType(person, "employee")
        dic["employee"] = employee

        customer = URIIOType(person, "customer")
        dic["customer"] = customer

        return dic

    """
    @description prints all types that are in this dictionary as a tree WITH all properties etc added
    """
    def printTypeManager(self):
        self.__print__(self.getType("type"), "")


    """
    @description a utility function to help the print() function
    @publicity private
    """
    def __print__(self, type, prefix):
        print(prefix + "-" + type.type)
        for tp in type.typeProperties:
            print(prefix + " * " + tp.type)
        for ap in type.atomicProperties:
            print(prefix + " * " + ap)
        for child in type.children:
            self.__print__(child, prefix + " | ")

    """
    @description prints all types that are in this dictionary as a tree but only displays typenames
    """
    def toString(self):
        return self.__str__(self.getType("type"), "")


    """
    @description a utility function to help the toString() function
    @publicity private
    """
    def __str__(self, type, prefix):
        str = prefix + "-" + type.type + "<br>"
        for child in type.children:
            str += self.__str__(child, prefix + " | ")
        return str