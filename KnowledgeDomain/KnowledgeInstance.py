__author__ = 'jeuna'

class KnowledgeInstance:
    def __init__(self, uriioManager, predicateManager):
        self.uriioManager = uriioManager
        self.predicateManager = predicateManager

    def asXML(self):
        toreturn = "<KnowledgeInstance>"
        toreturn += self.uriioManager.uriiosAsXML()
        toreturn += self.predicateManager.predicatesAsXML()
        toreturn += "</KnowledgeInstance>"
        return toreturn