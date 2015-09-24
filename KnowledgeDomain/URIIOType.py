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
@author jonathan langens
@created 18/08/2015
@description the URIIOType class is meant to describe types and type hierarchy in an organised way. In some respect it c
an be thought of as just a taxonomy. But it also adds properties and 3 operations that are beyond basics:
(1) condense:
when a type condenses it just throws all information about it in 1 condensed type form (you can think of this as what wo
uld be found in an encyclopedia)
(2) evolve:
the type creates a sibling and gives it back to the caller of the function. This can be used efficiently if types are di
scovered that need extra properties or less.
(3) purge:
when a type purges it checks it children to see if they share properties. If all children share a property then this pro
perty belongs to the parent type. If some children share properties then an in between type needs to be added.
"""
class URIIOType:

    """
    @param parent if this type is the base type of which all other types are subtypes then parent is none, otherwise the
    parent parameter is itself also a URIIOType
    @param type a string representation of the name of the type
    @pre the parent has to be initialised if isnt None and the name should be unique to this type
    @post a fully initialized type
    """
    def __init__(self, parent, type):
        self.children = []
        self.parent = parent
        if parent is not None:
            self.parent.children.append(self)
        self.type = type
        self.properties = []# these are just the properties
        self.locked = False# human users can set a type to locked if they are sure that it is definite
        self.systemDefined = False#A system defined type cannot be altered

    """
    @description this returns a list of all the types this type is (ie if the type is dog its also mamal, creature,...)
    @return a list of type this type is
    """
    def asTypeList(self):
        list = []
        if self.parent != None:
            list.extend(self.parent.asTypeList())
        list.append(self.type)
        return list

    """
    @description returns all properties this type has and all properties of all of its parent
    """
    def asPropertyList(self):
        list = []
        if self.parent != None:
            list.extend(self.parent.asPropertyList())
        list.extend(self.properties)
        return list

    """
    @para type the typename
    @return True if this type is the passed typename or a subtype of a type with this typename
    """
    def isOfType(self, type):
        if self.type == type:
            return True
        if self.parent is not None:
            return self.parent.isOfType(type)
        return False

    """
    @param atomicProperty the name of the property we want to check this type has
    @return True
    """
    def hasProperty(self, propertyname):
        for p in self.properties:
            if p.name == propertyname:
                return True
        if self.parent is not None:
            return self.parent.hasProperty(propertyname)
        return False

    """
    @param atomicProperty the name of the property we want to receive
    @return the property
    """
    def getProperty(self, propertyname):
        for p in self.properties:
            if p.name == propertyname:
                return p
        if self.parent is not None:
            return self.parent.hasAtomicProperty(propertyname)
        return None

    """
    @param name the name of the property we want to add (or alter)
    @param type the type of the named property
    @result this type has a property with that name and that type
    """
    def addProperty(self, name, type = KnowledgeDomainDefinitions.TEXT):
        if self.hasProperty(name):
            self.getProperty(name).type = type
        else:
            self.properties.append(URIIOTypeProperty(name, type))

    """
    @param propertyname the name of the property that should be remove
    @post there is no more property in this types property list with the given name
    """
    def removeProperty(self, propertyname):
        props2remove = []
        for p in self.properties:
            if p.name == propertyname:
                props2remove.append(p)

        for p in props2remove:
            self.properties.remove(p)

    """
    @return all the other children of this URIIO's parent
    """
    def getSiblings(self):
        siblings = self.parent.children.copy
        siblings.remove(self)
        return siblings

    """

    """
    def condense(self):
        supertypes = self.asTypeList()
        supertypes.remove(self.type)
        atomlist = self.asPropertyList()
        condesed = URIIOCondensedType(self.type, supertypes, atomlist)
        return condesed

    def evolve(self):
        parent = self.parent
        if len(self.children) > 0:
            parent = self
        evolution = URIIOType(parent, self.type + "x")
        for ap in self.properties:
            evolution.properties.append(URIIOTypeProperty(ap.name, ap.type))
        return evolution

    def purge(self):
        # if this type is locked we only pass the purge to its children
        if self.locked:
            for child in self.children:
                child.purge()
                return

        # first remove all properties that already appear in parents
        for child in self.children:
            aprops = []
            for atomprop in child.properties:
                if self.hasProperty(atomprop.name):
                    aprops.append(atomprop)

            for atomprop in aprops:
                child.properties.remove(atomprop)

        for child in self.children:
            """
            for typeprop in child.typeProperties:
                occuranceList = []
                for child in self.children:
                    if child.typeProperties.count(typeprop):
                        occuranceList.append(child)
                if len(occuranceList) ==  len(self.children) and len(self.children) > 1:
                    self.__extractFromChildren(typeprop, None)
                else:
                    if len(occuranceList) > 2 and len(occuranceList) > len(self.children) * 0.75:
                        self.__createSubtypeForProperty(occuranceList)
                occuranceList.clear()
                """

            for atomprop in child.properties:
                occuranceList2 = []
                for child in self.children:
                    if child.hasProperty(atomprop.name):
                        occuranceList2.append(child)
                if len(occuranceList2) == len(self.children) and len(self.children) > 1:
                    self.__extractFromChildren(atomprop)
                else:
                    if len(occuranceList2) > 2 and len(occuranceList2) > len(self.children) * 0.75:
                        self.__createSubtypeForProperty(occuranceList2)
                occuranceList2.clear()

        for child in self.children:
            child.purge()

    # helper function that extracts a property from all children of a type and injects it into the supertype
    def __extractFromChildren(self,  property):
        if property is not None:
            self.properties.append(property)
            for child in self.children:
                child.removeProperty(property.name)

    # helper function that defines that a subgroup of children from a type will fall under a new subclass of that type
    def __createSubtypeForProperty(self, listOfChildren):
        newType = URIIOType(self, self.type + "0")
        for child in listOfChildren:
            self.children.remove(child)
            child.parent = newType
        newType.children = listOfChildren

"""
a condensed type is just an 'instantiation' of a type, it will return an object that knows
its supertypes and has all properties it needs to have
you can think of a
"""
class URIIOCondensedType:
    def __init__(self, type, supertypes, properties):
        self.type = type
        self.supertypes = supertypes
        # we want the type properties to be condensed in this case as well
        self.typeProperties = []
        self.properties = properties

    def isOfType(self, type):
        if self.type == type:
            return True
        for t in self.supertypes:
            if t == type:
                return True
        return False

    def hasProperty(self, propertyname):
        for ap in self.properties:
            if ap.name == propertyname:
                return True
        return False

    def printType(self):
        print("type: " + self.type)
        print("| supertypes: ")
        for st in self.supertypes:
            print("| - " + st)
        print("|")
        print("| properties:")
        for ap in self.properties:
            print("| * " + ap.name + "(" + ap.type + ")")

"""
a URIIOType Property consists of a property name and a property type.
"""
class URIIOTypeProperty:
    def __init__(self, name, type = KnowledgeDomainDefinitions.TEXT):
        self.name = name
        self.type = type