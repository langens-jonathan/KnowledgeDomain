__author__ = 'Jonathan Langens'
from URIIOManager import URIIOManager
from URIIOTypeManager import URIIOTypeManager
from URIIOPredicateDefinitionManager import URIIOPredicateDefinitionManager
"""
@author Jonathan Langens
@description A Knowledge Domain describes an entire system of knowledge, it consists of:
             (1) URIIO's
             (2) data sources
             (3) a Type Hierarchy
             (4) predicate definitions
             (5) predicates
             (6) rules
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
        self.predicateManager = URIIOPredicateDefinitionManager(self.typeManager)

    """
    @description simple helper function that allows the domain to be easily printed to the terminal
    """
    def printKnowledgeDomain(self):
        print("KnowledgeDomain " + self.domain)
        print("type hierarchy")
        self.typeManager.printTypeManager()
        print("predicates")
        self.predicateManager.printPredicateDefinitionManager()
        print("URIIO's")
        self.URIIOManager.printURIIOManager()