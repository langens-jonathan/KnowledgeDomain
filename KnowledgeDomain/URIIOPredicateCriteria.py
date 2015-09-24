__author__ = 'Jonathan Langens'

class URIIOPredicateCriteria:
    def __init__(self, predicateList):
        self.predicates = predicateList

    def resolve(self):
        return self.predicates

