__author__ = 'Jonathan Langens'

class URIIOPredicate:
    def __init__(self, name, description, reflective, transitive, subject, object, systemDefined):
        self.name = name
        self.reflective = reflective
        self.transitive = transitive
        self.description = description
        self.subject = subject
        self.object = object
        self.systemDefined = systemDefined