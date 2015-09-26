__author__ = 'jeuna'

from DataSource import DataSource

class DataSourceXLSX(DataSource):
    def __init__(self, filename):
        self.template = SpreadSheetTemplate()
        self.sourceFile = "/home/jeuna/Downloads/datasources/wb.xlsx"

    def extendKnowledgeInstance(self, instance, URIIOCriteria, URIIOPredicateCriteria):
        return False