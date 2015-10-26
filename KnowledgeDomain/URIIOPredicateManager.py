__author__ = 'jeuna'
from URIIOPredicate import URIIOPredicate
"""
Copyright (C) 2015  Langens Jonathan

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
class URIIOPredicateManager:
    def __init__(self):
        self.predicates = []

    def containsPredicate(self, subject, predicate, object):
        for p in self.predicates:
            if p.subject.URI == subject.URI and p.predicate.name == predicate.name and p.object.URI == object.URI:
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

    def predicatesAsXML(self):
        toret = ""
        for p in self.predicates:
            toret += "<predicate>"
            toret += "<subject>" + p.subject.URI + "</subject>"
            toret += "<predicate>" + p.predicate.name + "</predicate>"
            toret += "<object>" + p.object.URI + "</object>"
            toret += "</predicate>"
        return toret