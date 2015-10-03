__author__ = 'Jonathan Langens'

class URIIOPredicateCriteria:
    def __init__(self, predicateList):
        self.predicates = predicateList

    def getCriteriaType(self):
        return "predicateCriteria"

    """
    resolve should go as it is no longer the  criterias job to do the filtering (the uriios and predicates are now
    being added instead of first adding all and the filtering out the unneceserry ones
    """
    def resolve(self):
        return self.predicates

