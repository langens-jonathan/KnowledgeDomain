__author__ = 'jeuna'
from KnowledgeInstance import KnowledgeInstance
from URIIOManager import URIIOManager
from URIIOPredicateManager import URIIOPredicateManager

class DataSourceManager:
    def __init__(self):
        self.sources = []

    def addDataSource(self, src):
        self.sources.append(src)

    def getKnowledgeInstance(self, uriioCritera, predicateCriteria):
        instance = KnowledgeInstance(URIIOManager("/tmp/user/"), URIIOPredicateManager())

        changed = False

        for src in self.sources:
            if src.extendKnowledgeInstance(instance, uriioCritera, predicateCriteria):
                changed = True

        while changed:
            changed = False
            for src in self.sources:
                if src.extendKnowledgeInstance(instance, uriioCritera, predicateCriteria):
                    changed = True

        return instance