__author__ = 'jeuna'
from KnowledgeDomain.User.UserBox import UserBox
from KnowledgeDomain.Criteria.Criteria import Criteria

class DataSource:

    # all DataSource object must override the following method. When passed an instance and 2 criteria the
    # datasource extends (or injects) all objects the qualify the criteria and all predicates that do
    # the extend knowledge instance function should be removed as it is partitioned in 4 parts now
    def extendKnowledgeInstance(self, instance, URIIOCriteria, URIIOPredicateCriteria, domain):
        return False


    def processPreQueries(self, userBox, criteria):
        return False

    def extractURIIOs(self, userBox, criteria):
        return False

    def processConnectors(self):
        return False