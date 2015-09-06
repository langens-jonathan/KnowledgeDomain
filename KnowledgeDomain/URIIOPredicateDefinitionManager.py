__author__ = 'Jonathan Langens'
from URIIOPredicateDefinition import URIIOPredicateDefinition
from URIIOTypeManager import URIIOTypeManager
from URIIOType import URIIOType

class URIIOPredicateDefinitionManager:
    def __init__(self, typeManager):
        self.typeManager = typeManager
        type = self.typeManager.getType('type')
        self.predicates = []
        self.predicates.append(URIIOPredicateDefinition("contains", "", False, True, type, type, True))
        self.predicates.append(URIIOPredicateDefinition("has", "", False, True, type, type, True))
        self.predicates.append(URIIOPredicateDefinition("refersTo", "", False, False, type, type, True))
        self.predicates.append(URIIOPredicateDefinition("isOfType", "", False, False, type, type, True))
        self.predicates.append(URIIOPredicateDefinition("mightBeOfType", "", False, False, type, type, True))
        self.predicates.append(URIIOPredicateDefinition("operatesOn", "", False, False, type, type, True))

    def printPredicateDefinitionManager(self):
        for pred in self.predicates:
            reftext = "reflective), ("
            trantext = "transitive)"
            if not pred.reflective:
                reftext = "not " + reftext
            if not pred.transitive:
                trantext = "not " + trantext
            print(pred.name + " (" + reftext + trantext)
            print("<" + pred.subject.type + "> " + pred.name + " <" + pred.object.type + ">")

    def getPredicate(self, predicate):
        for p in self.predicates:
            if p.name == predicate:
                return p
        return None

    def addPredicate(self, name, description, reflective, transitive, subject, object):
        sub = self.typeManager.getType(subject)
        obj = self.typeManager.getType(object)
        pred = self.getPredicate(name)
        if pred is not None:
            pred.description = description
            pred.reflective = reflective
            pred.transitive = transitive
            pred.subject = sub
            pred.object = obj
        else:
            self.predicates.append(URIIOPredicateDefinition(name, description, reflective, transitive, sub, obj, False))