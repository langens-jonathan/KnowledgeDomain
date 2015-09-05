__author__ = 'Jonathan Langens'

from KnowledgeDomain.KnowledgeDomain import KnowledgeDomain

class KnowledgeDomainManager:

    DOMAIN = None
    def __init__(self):
        if KnowledgeDomainManager.DOMAIN  is None:
            KnowledgeDomainManager.DOMAIN = KnowledgeDomain("172.0.0.1")

    @classmethod
    def getDomain(self):
        return KnowledgeDomainManager.DOMAIN