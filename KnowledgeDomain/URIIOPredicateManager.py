__author__ = 'Jonathan Langens'
from KnowledgeDomain.URIIOPredicate import URIIOPredicate
from KnowledgeDomain.URIIOTypeManager import URIIOTypeManager
from KnowledgeDomain.URIIOType import URIIOType

class URIIOPredicateManager:
    def __init__(self, typeManager):
        self.typeManager = typeManager
        type = self.typeManager.getType('type')
        self.predicates = []
        self.predicates.append(URIIOPredicate("contains", "", False, True, type, type, True))
        self.predicates.append(URIIOPredicate("has", "", False, True, type, type, True))
        self.predicates.append(URIIOPredicate("refersTo", "", False, False, type, type, True))
        self.predicates.append(URIIOPredicate("isOfType", "", False, False, type, type, True))
        self.predicates.append(URIIOPredicate("mightBeOfType", "", False, False, type, type, True))
        self.predicates.append(URIIOPredicate("operatesOn", "", False, False, type, type, True))

    def print(self):
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
            self.predicates.append(URIIOPredicate(name, description, reflective, transitive, sub, obj, False))