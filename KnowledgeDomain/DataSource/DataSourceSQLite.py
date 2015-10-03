__author__ = 'jeuna'
from KnowledgeDomain.DataSource.DataSource import DataSource
from KnowledgeDomain.Template.TemplateSQLite import TemplateSQLite
from KnowledgeDomain.Template.TemplateSQLite import SQLTable
from KnowledgeDomain.Template.TemplateSQLite import SQLColumn

import sqlite3 as lite

class DataSourceSQLite(DataSource):
    def __init__(self, filename):
        self.sourceFile = filename
        self.template = TemplateSQLite()

    def addURIIOS(self, instance, URIIOCriteria, domain):
        for table in self.template.tables:
            utype = domain.typeManager.getType(table.type)
            if utype is None:
                utype = domain.typeManager.getType("type")
            rows = self.getRowsInTable(table.name)

            for row in rows:
                uriio = instance.uriioManager.newURIIO()
                uriio.addType(utype)
                for col in table.columns:
                    uriio.addProperty(col.name, row[col.number], "text")

        return True

    def getConnection(self):
        try:
            return lite.connect('/home/jeuna/Downloads/datasources/data.db')
        except ValueError:
            print("SQLLite connection refused")

        return None

    def getRowsInTable(self, tablename):
        cur = self.getConnection().cursor()
        cur.execute("SELECT * FROM " + tablename)
        return cur.fetchall()
