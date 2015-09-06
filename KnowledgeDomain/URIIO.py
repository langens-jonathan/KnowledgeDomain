__author__ = 'Jonathan Langens'

"""
@classname URIIdentifiedObject
@author Jonathan Langens
@created 17/08/2015
@version 0.01
@description A URI Identified Object is a generic class that describes an object or an idea
             It contains of a URI that identifies this object, and of three lists. A list with
             types (ontae) of which the most definite type is positioned at the last position and
             the most general type (URIIO) is at position 0. A list of properties of type URIProperty
             and a list of predicates of type URIPredicate
"""

class URIIO:

    """
    @param URI the URI that gets passed to the constructor should be unique
    @pre a unique URI has to be passed
    @post the URI_Identified_Object is correctly initialized with a unique URI and with the URIIO type set at ontae[0]
    """
    def __init__(self, URI):
        self.URI = URI
        # self.ontae = []
        # self.ontae.append("URIIO")
        self.properties = []
        self.predicates = []

    """
    @param ontos the type that will be added to the list of types. We consider the latest passed type as the most defini
    te
    @pre self.ontae contains all more general types that the object has
    @post self.ontae.last = ontos
    """
    """
    def addOntos(self, ontos):
        self.ontae.append(ontos)
    """
    """
    @param type the type that will be added to the list of types. We consider the latest passed type as the most definit
    e
    @pre self.ontae contains all more general types that the object has
    @post self.ontae.last = type
    """
    """
    def addType(self, type):
        self.ontae.append(type)
    """
    """
    @param ontae a list of types that will be used as the type list, the list item in this list is the definite type
    @post self.ontae.last = type
    """
    """
    def setOntae(self, ontae):
        self.ontae = ontae
    """
    """
    @param name the name of the property (i.e. for car.color we would use "color" for the name)
    @param value the value of the property(i.e. for a red color we would use "red" for the value)
    @post the property is initialized as a URIProperty with name and value
    """
    def addProperty(self, name, value):
        prop = self.getProperty(name)
        if prop == None:
            self.properties.append(URIProperty(name, value))
        else:
            prop.value = value


    """
    @param name the name of the property you wish to retrieve
    @return if this URIIO contains a property with the given name then that property else None
    """
    def getProperty(self, name):
        for p in self.properties:
            if p.name == name:
                return p
        return None

    """
    @param name the name of the property that should be removed
    @post if the property is found it is removed
    """
    def removeProperty(self, name):
        prop = self.getProperty(name)
        if prop is not None:
            self.properties.remove(prop)

    """
    @param predicate a URIIO that describes this predicate
    @param object a URIIO that describes the object
    @post this method is always called on the URIIO that is supposed to be the subject of the predicate. This method the
    n adds a predicate of this form to the object
    """
    def addPredicate(self, predicate, object):
        self.predicates.append(URIPredicate(predicate, object))

    """
    @description this function converts the this URIIO to a list of simple triples
    """
    def convertToTriples(self):
        triples = []

        # first convert the ontae to triples
        #for ontos in self.ontae:
        #    triples.append(simpleTriple(self.URI, "isOfType", ontos))

        # then convert all the properties to triples
        for property in self.properties:
            triples.append(simpleTriple(self.URI, property.name, property.value))

        # lastly convert the predicates
        for predicate in self.predicates:
            triples.append(simpleTriple(self.URI, predicate.predicate.URI, predicate.object.URI))

        return triples


"""
@classname URI Property
@author Jonathan Langens
@created 17/08/2015
@version 0.01
@description a small helper class that defines a property as 2 strings
"""
class URIProperty:
    def __init__(self, name, value):
        self.name = name
        self.value = value

"""
@classname URI Predicate
@author Jonathan Langens
@created 17/08/2015
@version 0.01
@description a small helper class that defines a predicate's predicate and object as 2 URIIO's
"""
class URIPredicate:
    def __init__(self, predicate, object):
        self.predicate = predicate
        self.object = object

"""
@classname simple triple
@author Jonathan Langens
@created 17/08/2015
@version 0.01
@description a small helper class that defines a simple triple as 3 strings and that provides a function to print it
"""
class simpleTriple:
    def __init__(self, subject, predicate, object):
        self.subject = subject
        self.predicate = predicate
        self.object = object

    def printTriple(self):
        print(self.subject + ' ' + self.predicate + ' ' + self.object)