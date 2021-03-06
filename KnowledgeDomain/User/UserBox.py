__author__ = 'jeuna'
from KnowledgeDomain.KnowledgeInstance import KnowledgeInstance
from KnowledgeDomain.URIIOManager import URIIOManager
from KnowledgeDomain.URIIOPredicateManager import URIIOPredicateManager
"""
The User Box is one user's work space, it will be set to allow certain maxima in terms of URIIOs and Predicates.
It stores the users Query results so the user can do usefull stuff with the data he queried. For now this class
will not be truly fleshed out well.
"""

class UserBox:
    def __init__(self, username):
        self.username = username
        self.maxURIIOs = 500
        self.maxPredicates = 2500
        self.knowledgeInstance = None
        self.canAddDataSources = False
        self.canPersistKnowledgeInstances = False

    def maxedOutURIIOs(self):
        return len(self.knowledgeInstance.uriioManager.URIIOs) >= self.maxURIIOs

    def maxedOutPredicates(self):
        return len(self.knowledgeInstance.predicateManagers.predicates) >= self.maxPredicates

    def resetKnowledgeInstance(self):
        self.knowledgeInstance = KnowledgeInstance(URIIOManager("/" + self.username), URIIOPredicateManager())