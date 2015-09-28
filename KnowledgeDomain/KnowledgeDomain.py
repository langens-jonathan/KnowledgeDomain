__author__ = 'Jonathan Langens'
from URIIOManager import URIIOManager
from URIIOTypeManager import URIIOTypeManager
from URIIOPredicateDefinitionManager import URIIOPredicateDefinitionManager
from URIIOPredicateManager import URIIOPredicateManager
from TemplateManager import TemplateManager
from DataSourceManager import DataSourceManager

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
@author Jonathan Langens
@description A Knowledge Domain describes an entire system of knowledge, it consists of:
             (1) URIIO's - fuzzy objects that can be firmly or loosely connected to a type
             (2) data sources
             (3) a Type Hierarchy
             (4) predicate definitions
             (5) predicates
             (6) rules
             (7) built-in time and geography support, this is done through typing
             Together they make up a knowledge system from different sources.
@version 0.01
"""
class KnowledgeDomain:

    """
    @parameter name the name that this domain will be addressed with, should be unique in the world
    @pre the passed name should be unique
    @post the domain is initialized, and all subsystems too
    """
    def __init__(self, name):
        self.domain = name
        self.URIIOManager = URIIOManager(self.domain)
        self.typeManager = URIIOTypeManager()
        self.predicateDefinitionManager = URIIOPredicateDefinitionManager(self.typeManager)
        self.predicateManager = URIIOPredicateManager()
        self.templateManager = TemplateManager()
        self.dataSourceManager = DataSourceManager()

    """
    @description simple helper function that allows the domain to be easily printed to the terminal
    """
    def printKnowledgeDomain(self):
        print("KnowledgeDomain " + self.domain)
        print("type hierarchy")
        self.typeManager.printTypeManager()
        print("predicates")
        self.predicateDefinitionManager.printPredicateDefinitionManager()
        print("URIIO's")
        self.URIIOManager.printURIIOManager()