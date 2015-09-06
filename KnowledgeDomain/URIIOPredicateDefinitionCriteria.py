__author__ = 'Jonathan Langens'
from URIIOPredicateDefinition import URIIOPredicateDefinition
from URIIOType import  URIIOType

class URIIOPredicateDefinitionCriteria:
    def __init__(self, predicateList):
        self.name = None
        self.reflective = None
        self.transitive = None
        self.subject = None
        self.object = None
        self.predicateList = predicateList

    def __clearBasedOnName(self):
        list = []
        for pred in self.predicateList:
            if not pred.name == self.name:
                list.append(pred)
        for pred in list:
            self.predicateList.remove(pred)

    def __clearBasedOnReflectiveness__(self):
        list = []
        for pred in self.predicateList:
            if not pred.reflective == self.reflective:
                list.append(pred)
        for pred in list:
            self.predicateList.remove(pred)

    def __clearBasedOnTransitivity__(self):
        list = []
        for pred in self.predicateList:
            if not pred.transitive == self.transitive:
                list.append(pred)
        for pred in list:
            self.predicateList.remove(pred)

    def __clearBasedOnSubject__(self):
        list = []
        for pred in self.predicateList:
            if not pred.subject == self.subject:
                list.append(pred)
        for pred in list:
            self.predicateList.remove(pred)

    def __clearBasedOnObject__(self):
        list = []
        for pred in self.predicateList:
            if not pred.object == self.object:
                list.append(pred)
        for pred in list:
            self.predicateList.remove(pred)

    def resolve(self):
        if self.name is not None:
            self.__clearBasedOnName()
        if self.reflective is not None:
            self.__clearBasedOnReflectiveness__()
        if self.transitive is not None:
            self.__clearBasedOnTransitivity__()
        if self.subject is not None:
            self.__clearBasedOnSubject__()
        if self.object is not None:
            self.__clearBasedOnObject__()