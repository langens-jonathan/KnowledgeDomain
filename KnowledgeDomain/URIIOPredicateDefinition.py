__author__ = 'Jonathan Langens'
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
class URIIOPredicateDefinition:
    def __init__(self, name, description, reflective, transitive, subject, object, systemDefined):
        self.name = name
        self.reflective = reflective
        self.transitive = transitive
        self.description = description
        self.subject = subject
        self.object = object
        self.systemDefined = systemDefined