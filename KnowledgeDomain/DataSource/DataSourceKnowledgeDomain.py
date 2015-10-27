__author__ = 'jonathan Langens'
from KnowledgeDomain.DataSource.DataSource import DataSource
from KnowledgeDomainServer.SocketFileReceiver import *
import socket
import xml.etree.cElementTree as ET

class DataSourceKnowledgeDomain(DataSource):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.overrideCurrentKnowledge = False

    def processPreQueries(self, userBox, criteria, domain):
        if self.overrideCurrentKnowledge:
            return True
        else:
            return True

    def extractURIIOs(self, userBox, criteria, domain):
        instance = userBox.knowledgeInstance
        uriioManager = instance.uriioManager


        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))

        URIIOQuery = "<KDSQuery><user>" + self.username + "</user><password>" + self.password + "</password><query><URIIOQuery></URIIOQuery></query></KDSQuery>"

        send_msg(client_socket, URIIOQuery)

        answer = recv_msg(client_socket)

        """
        extract the urriio's here... it would probably be an awesome idea to check wheter the uri exists here. If we do the same in the pre query range
        we can basicly only add currently unknown URIIO's here with the URI from THEIR knowledge domain as it is and in our prequery range we can override
        our knowledge IF the correct flag on this datasource is set
        """


        return True

    def processConnectors(self, userBox, criteria, domain):
        return True