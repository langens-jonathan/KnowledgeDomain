__author__ = 'jeuna'

class URIIOPredicate:
    def __init__(self, subjet, predicate, object):
        self.subject = subjet
        self.object = object
        self.predicate = predicate

    def getObjects(self):
        objects = []
        objects.append(self.object)
        if self.predicate.reflective:
            objects.append(self.subject)
        return objects

    def getSubjects(self):
        subjects = []
        subjects.append(self.subject)
        if self.predicate.reflective:
            subjects.append(self.object)
        return subjects
