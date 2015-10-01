__author__ = 'jeuna'
from Template import Template
from URIIO import URIIO

class TemplateSQLite(Template):

    def __init__(self):
        self.tables = []

    def getHashCode(self):
        return "SQLiteHash"


class SQLTable:
    def __init__(self, name):
        self.columns = []
        self.name = name
        self.type = "type"

    def addColumn(self, name , number):
        self.columns.append(SQLColumn(name, number))


class SQLColumn:
    def __init__(self, name, number):
        self.name = name
        self.number = number