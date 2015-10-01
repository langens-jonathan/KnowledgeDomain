__author__ = 'jeuna'
from KnowledgeInstance import KnowledgeInstance
from URIIOManager import URIIOManager
from URIIOPredicateManager import URIIOPredicateManager

class DataSourceManager:
    def __init__(self):
        self.sources = []

    def addDataSource(self, src):
        self.sources.append(src)

    def getKnowledgeInstance(self, uriioCritera, predicateCriteria, domain):
        instance = KnowledgeInstance(URIIOManager("/tmp/user/"), URIIOPredicateManager())

        changed = False

        sources = []

        print("number of data sources = " + str(len(self.sources)))

        for src in self.sources:
            if src.extendKnowledgeInstance(instance, uriioCritera, predicateCriteria, domain):
                changed = True
            else:
                sources.append(src)

        sourcesThatChangedTheKI = []
        while changed:
            changed = False
            for src in sources:
                if src.extendKnowledgeInstance(instance, uriioCritera, predicateCriteria, domain):
                    changed = True
                    sourcesThatChangedTheKI.append(src)

            for src in sourcesThatChangedTheKI:
                sources.remove(src)

            sourcesThatChangedTheKI = []

        return instance