__author__ = 'Jonathan Langens'
from URIIOPredicateDefinition import URIIOPredicateDefinition
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

    def asXML(self):
        output = "<predicateDefinitions>"
        for p in self.predicateList:
            output += "<predicateDefinition>"
            output += "<name>" + p.name + "</name>"
            ref = "true"
            if p.reflective is False:
                ref = "false"
            output += "<reflective>" + ref + "</reflective>"
            tran = "true"
            if p.transitive is False:
                tran = "false"
            output += "<transitive>" + tran + "</transitive>"
            output += "<subject>" + p.subject.type + "</subject>"
            output += "<object>" + p.object.type + "</object>"
            output += "</predicateDefinition>"
        output += "</predicateDefinitions>"
        return output