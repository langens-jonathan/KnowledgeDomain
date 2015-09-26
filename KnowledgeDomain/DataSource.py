__author__ = 'jeuna'

class DataSource:

    # all DataSource object must override the following method. When passed an instance and 2 criteria the
    # datasource extends (or injects) all objects the qualify the criteria and all predicates that do
    def extendKnowledgeInstance(self, instance, URIIOCriteria, URIIOPredicateCriteria):
        return False