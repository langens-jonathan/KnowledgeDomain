__author__ = 'jeuna'

class DataSource:

    # all DataSource object must override the following method. When passed an instance and 2 criteria the
    # datasource extends (or injects) all objects the qualify the criteria and all predicates that do
    # the extend knowledge instance function should be removed as it is partitioned in 4 parts now
    def extendKnowledgeInstance(self, instance, URIIOCriteria, URIIOPredicateCriteria, domain):
        return False


    def processPreQueries(self):
        return False

    def extractURIIOs(self):
        return False

    def processConnectors(self):
        return False