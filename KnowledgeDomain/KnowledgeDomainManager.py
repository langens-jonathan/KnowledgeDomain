__author__ = 'Jonathan Langens'

from KnowledgeDomain import KnowledgeDomain
"""
@author Jonathan Langens
@description The knowledge domain manager initializes a singleton knowledge domain
@version 0.01
"""
class KnowledgeDomainManager:

    DOMAIN = None
    """
    @post the only domain gets initialised if it did not exist before
    """
    def __init__(self):
        if KnowledgeDomainManager.DOMAIN  is None:
            KnowledgeDomainManager.DOMAIN = KnowledgeDomain("172.0.0.1")

    """
    @return the singleton domain
    """
    @classmethod
    def getDomain(self):
        return KnowledgeDomainManager.DOMAIN