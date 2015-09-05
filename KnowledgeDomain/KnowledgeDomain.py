__author__ = 'Jonathan Langens'
from KnowledgeDomain.URIIOManager import URIIOManager
from KnowledgeDomain.URIIOTypeManager import URIIOTypeManager
from KnowledgeDomain.URIIOPredicateManager import URIIOPredicateManager
"""
@author Jonathan Langens
"""
class KnowledgeDomain:

    def __init__(self, name):
        self.domain = name
        self.URIIOManager = URIIOManager(self.domain)
        self.typeManager = URIIOTypeManager()
        self.predicateManager = URIIOPredicateManager(self.typeManager)

    def print(self):
        print("KnowledgeDomain " + self.domain)
        print("type hierarchy")
        self.typeManager.print()
        print("predicates")
        self.predicateManager.print()
        print("URIIO's")
        self.URIIOManager.print()