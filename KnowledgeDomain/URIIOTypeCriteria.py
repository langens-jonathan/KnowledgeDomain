__author__ = 'Jonathan Langens'
from KnowledgeDomain.URIIOType import  URIIOType

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

    def __clearBasedOnType__(self):
        list = []
        for tp in self.typeList:
            if not tp.isOfType(self.type):
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