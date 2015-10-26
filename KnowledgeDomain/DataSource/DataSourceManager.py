__author__ = 'jeuna'
from KnowledgeDomain.KnowledgeInstance import KnowledgeInstance
from KnowledgeDomain.URIIOManager import URIIOManager
from KnowledgeDomain.URIIOPredicateManager import URIIOPredicateManager

class DataSourceManager:
    def __init__(self):
        self.sources = []

    def addDataSource(self, src):
        self.sources.append(src)

    """
    def getKnowledgeInstance(self, uriioCritera, predicateCriteria, domain):
        instance = KnowledgeInstance(URIIOManager("/tmp/user"), URIIOPredicateManager())

        changed = False

        sources = []

        for src in self.sources:
            if src.addURIIOS(instance, uriioCritera, domain):
                changed = True
            else:
                sources.append(src)

        sourcesThatChangedTheKI = []
        while changed:
            changed = False
            for src in sources:
                if src.addURIIOS(instance, uriioCritera, domain):
                    changed = True
                    sourcesThatChangedTheKI.append(src)

            for src in sourcesThatChangedTheKI:
                sources.remove(src)

            sourcesThatChangedTheKI = []

        for src in self.sources:
            src.addPredicates(instance, None, domain)

        return instance
    """
    def addToKnowledgeInstance(self, userBox, criteria, domain):
        # first process prequeries
        for src in self.sources:
            src.processPreQueries(userBox, criteria, domain)

        # then extract the uriios
        for src in self.sources:
            src.extractURIIOs(userBox, criteria, domain)

        # lastly process the connectors (adding relevant predicates and extending certain uriios)
        for src in self.sources:
            src.processConnectors(userBox, criteria, domain)