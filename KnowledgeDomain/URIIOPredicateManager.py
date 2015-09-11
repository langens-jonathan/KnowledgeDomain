__author__ = 'jeuna'
from URIIOPredicate import URIIOPredicate

class URIIOPredicateManager:
    def __init__(self):
        self.predicates = []

    def containsPredicate(self, subject, predicate, object):
        for p in self.predicates:
            if p.subject == predicate.subject and p.predicate == predicate.predicate and p.object == predicate.object:
                return p
        return None

    def addPredicate(self, subject, predicate, object):
        if self.containsPredicate(subject, predicate, object) is None:
            self.predicates.append(URIIOPredicate(subject, predicate, object))

    def removePrediate(self, predicate):
        self.predicates.remove(predicate)

    def removePredicate(self, subject, predicate, object):
        p = self.containsPredicate(subject, predicate, object)
        if p is not None:
            self.removePrediate(p)

    def getCardinality(self, uriio):
        cardinality = 0
        for p in self.predicates:
            if p.object == uriio or p.subject == uriio:
                ++cardinality
        return cardinality

    def getPredicatesForURIIO(self, uriio):
        predicates = []
        for p in self.predicates:
            if p.object == uriio or p.subject == uriio:
                predicates.append(p)
        return predicates

    def getPredicatesForPredicateDefinition(self, preddef):
        predicates = []
        for p in self.predicates:
            if p.predicate == preddef:
                predicates.append(p)
        return predicates