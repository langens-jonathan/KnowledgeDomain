__author__ = 'jeuna'
from TemplateXLSX import TemplateXLSX
from DataSource import DataSource

class DataSourceXLSX(DataSource):
    def __init__(self, filename):
        self.template = TemplateXLSX()
        self.sourceFile = "/home/jeuna/Downloads/datasources/wb.xlsx"

    def extendKnowledgeInstance(self, instance, URIIOCriteria, URIIOPredicateCriteria):
        return False