__author__ = 'jeuna'
from DataSource import DataSource

class DataSourceSQLite(DataSource):
    def __init__(self, filename):
        self.sourceFile = filename

    def extendKnowledgeInstance(self, instance, URIIOCriteria, URIIOPredicateCriteria):
        return False