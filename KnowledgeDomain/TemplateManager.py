__author__ = 'jeuna'
from Template import Template
class TemplateManager:
    def __init__(self):
        self.templates = dict()

    def setTemplate(self, template):
        ht = template.getHashCode()
        self.templates.setdefault(ht, template)

    def getTemplate(self, hashCode):
        return self.templates.get(hashCode)