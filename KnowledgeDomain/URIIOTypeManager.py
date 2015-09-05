__author__ = 'Jonathan Langens'
from KnowledgeDomain.URIIOType import URIIOType

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
        if type.systemDefined:
            return
        etype = self.getType(type)
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
    def getNewURIIO(self, parent, name):
        p = self.getType(parent)
        nType = URIIOType(p, name)
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
    def print(self):
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