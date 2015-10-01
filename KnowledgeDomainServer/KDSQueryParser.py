__author__ = 'Jonathan Langens'
import xml.etree.cElementTree as ET

from KnowledgeDomain.KnowledgeDomainManager import KnowledgeDomainManager
from KnowledgeDomain.URIIOType import URIIOType
from KnowledgeDomain.URIIOType import URIIOTypeProperty
from KnowledgeDomain.TemplateXLSX import TemplateXLSX
from KnowledgeDomain.TemplateXLSX import XLSXObjectPropertyTemplate
from KnowledgeDomain.TemplateXLSX import XLSXObjectTemplate
from KnowledgeDomain.TemplateXLSX import XLSXObjectConnectorTemplate
from KnowledgeDomain.DataSourceXLSX import DataSourceXLSX
from KnowledgeDomain.URIIOCriteria import URIIOCriteria

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
def ParseQuery(query):
    base = ET.fromstring(query)

    usr = ""
    pwd = ""
    root = None
    for child in base:
        if child.tag == "user":
            usr = child.text
        elif child.tag == "password":
            pwd = child.text
        elif child.tag == "query":
            for ch in child:
                root = ch

    if not usr == "jonathan" or not pwd == "is de beste":
        return "<failed>U have not authenticated</failed>"

    #
    # URIIO related stuff
    #
    if root.tag == "URIIOQuery":
        return processURIIOQuery(root)
    elif root.tag == "actionURIIONew":
        return processURIIONew(root)
    elif root.tag == "actionURIIODelete":
        return processURIIODelete(root)
    elif root.tag == "actionURIIOAddProperty":
        return processURIIOAddProperty(root)
    elif root.tag == "actionURIIORemoveProperty":
        return processURIIORemoveProperty(root)
    elif root.tag == "actionURIIOAddType":
        return processURIIOAddType(root)
    elif root.tag == "actionURIIOSetType":
        return processURIIOSetType(root)
    elif root.tag == "actionURIIORemoveType":
        return processURIIORemoveType(root)
    elif root.tag == "cardinalityForURIIO":
        return processCardinalityForURIIO(root)


    #
    # Predicate Definition related stuff
    #
    elif root.tag == "predicateDefinitionQuery":
        return processPredicateDefinitionQuery(root)
    elif root.tag == "actionPredicateDefinition":
        return processPredicateDefinition(root)
    elif root.tag == "actionPredicateDefinitionDelete":
        return processPredicateDefinitionDelete(root)

    #
    # URIIO TYPE related stuff
    #
    elif root.tag == "URIIOTypeQuery":
        return processURIIOTypeQuery(root)
    elif root.tag == "URIIOCondensedTypeQuery":
        return processURIIOCondensedTypeQuery(root)
    elif root.tag == "URIIOBaseTypeQuery":
        return processURIIOBaseTypeQuery(root)
    elif root.tag == "URIIOTypeGetSubTypesQuery":
        return processURIIOSubTypesQuery(root)
    elif root.tag == "actionURIIOTypePurge":
        return processURIIOTypePurge(root)
    elif root.tag == "actionURIIOTypeEvolve":
        return processURIIOTypeEvolve(root)
    elif root.tag == "actionURIIOTypeDelete":
        return processURIIOTypeDelete(root)
    elif root.tag == "actionURIIOTypeSave":
        return processURIIOTypeSave(root)

    #
    # Predicate Related stuff
    #

    elif root.tag == "predicateQuery":
        return processPredicateQuery(root)
    elif root.tag == "predicateURIQuery":
        return processPredicateURIQuery(root)
    elif root.tag == "actionAddPredicate":
        return processAddPredicate(root)
    elif root.tag == "actionRemovePredicate":
        return processRemovePredicate(root)

    #
    # Template Related Stuff
    elif root.tag == "actionTemplateSave":
        return processSaveTemplate(root)


    #
    # DataSource Related Stuff
    #
    elif root.tag == "actionDataSourceSave":
        return processSaveDataSource(root)


    return "unable to process query of type: " + root.tag + "\nFor more info on queries consult the documentation."

#
# URIIO Related stuff
#

"""
def processURIIOQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    criteria = kd.URIIOManager.getCriteria()

    for child in root:
        if child.tag == "type":
            criteria.TypeRestrictions.append(child.text)
        elif child.tag == "property":
            name = ""
            value = ""
            for propdef in child:
                if propdef.tag == "name":
                    name = propdef.text
                elif propdef.tag == "value":
                    value = propdef.text
            criteria.addPropertyRestriction(name, value)
        elif child.tag == "predicate":
            pred = ""
            obj = ""
            for preddef in child:
                if preddef.tag == "name":
                    pred = preddef.text
                elif preddef.tag == "object":
                    obj = preddef.text
            criteria.addPredicateRestrition(pred, obj)
        elif child.tag == "uriio":
            criteria.addURIRestriction(child.text)

    criteria.resolve()

    return criteria.asXML()
"""
def processURIIOQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()

    criteria = URIIOCriteria([])

    for child in root:
        if child.tag == "type":
            criteria.TypeRestrictions.append(child.text)
        elif child.tag == "property":
            name = ""
            value = ""
            for propdef in child:
                if propdef.tag == "name":
                    name = propdef.text
                elif propdef.tag == "value":
                    value = propdef.text
            criteria.addPropertyRestriction(name, value)
        elif child.tag == "predicate":
            pred = ""
            obj = ""
            for preddef in child:
                if preddef.tag == "name":
                    pred = preddef.text
                elif preddef.tag == "object":
                    obj = preddef.text
            criteria.addPredicateRestrition(pred, obj)
        elif child.tag == "uriio":
            criteria.addURIRestriction(child.text)

    instance = kd.dataSourceManager.getKnowledgeInstance(criteria, None, kd)
    criteria.URIIOList = instance.uriioManager.URIIOs
    return criteria.asXML()


def processURIIONew(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uriio = kd.URIIOManager.newURIIO()
    return uriio.asXML()

def processURIIODelete(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    for child in root:
        if child.tag == "URI":
            kd.URIIOManager.removeURIIO(child.text)
    return "<success></sucess>"

def processURIIOAddProperty(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    propname = ""
    propvalue = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
        elif child.tag == "property":
            for propdef in child:
                if propdef.tag == "name":
                    propname = propdef.text
                elif propdef.tag == "value":
                    propvalue = propdef.text
    uriio = kd.URIIOManager.getURIIO(uri)
    uriio.addProperty(propname, propvalue)
    return "<success></sucess>"

def processURIIORemoveProperty(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    propname = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
        elif child.tag == "property":
            for propdef in child:
                if propdef.tag == "name":
                    propname = propdef.text
    uriio = kd.URIIOManager.getURIIO(uri)
    uriio.removeProperty(propname)
    return "<success></sucess>"

def processURIIOAddType(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    type = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
        elif child.tag == "type":
            type = child.text
    uriio = kd.URIIOManager.getURIIO(uri)
    uriio.type.append(kd.typeManager.getType(type))
    return "<success></sucess>"

def processURIIOSetType(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    type = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
        elif child.tag == "type":
            type = child.text
    uriio = kd.URIIOManager.getURIIO(uri)
    uriio.type = []
    uriio.type.append(kd.typeManager.getType(type))
    return "<success></sucess>"

def processURIIORemoveType(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    type = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
        elif child.tag == "type":
            type = child.text
    uriio = kd.URIIOManager.getURIIO(uri)
    tp = kd.typeManager.getType(type)
    uriio.type.remove(tp)
    return "<success></sucess>"

def processCardinalityForURIIO(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
    uriio = kd.URIIOManager.getURIIO(uri)
    if uriio is not None:
        return "<cardinality><uri>" + uri + "</uri><cardinality>" + str(kd.predicateManager.getCardinality(uriio)) + "</cardinality></cardinality>"

#
# Predicate Definition related stuff
#

def processPredicateDefinitionQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    criteria = kd.predicateDefinitionManager.getCriteria()
    for child in root:
        if child.tag == "name":
            criteria.name = child.text
        elif child.tag == "reflective":
            if child.text == "true":
                criteria.reflective = True
            else:
                criteria.reflective = False
        elif child.tag == "transitive":
            if child.text == "true":
                criteria.transitive = True
            else:
                criteria.transitive = False
        elif child.tag == "subject":
            if kd.typeManager.getType(child.text) is not None:
                criteria.subject = kd.typeManager.getType(child.text)
        elif child.tag == "object":
            if kd.typeManager.getType(child.text) is not None:
                criteria.object = kd.typeManager.getType(child.text)
    criteria.resolve()
    return criteria.asXML()

def processPredicateDefinition(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    name = ""
    description = ""
    reflective = False
    transitive = False
    subject = None
    object = None
    for child in root:
        if child.tag == "name":
            name = child.text
        elif child.tag == "description":
            description = child.text
        elif child.tag == "reflective":
            if child.text == "true":
                reflective = True
        elif child.tag == "transitive":
            if child.text == "true":
                transitive = True
        elif child.tag == "subject":
            if kd.typeManager.getType(child.text) is not None:
                subject = child.text
        elif child.tag == "object":
            if kd.typeManager.getType(child.text) is not None:
                object = child.text

    if object == "":
        return "<failed>The type <" + object + "> is not a known type in this knowledge domain</failed>"
    if subject == "":
        return "<failed>The type <" + subject + "> is not a known type in this knowledge domain</failed>"
    if name == "":
         return "<failed>No name passed!</failed>"

    kd.predicateDefinitionManager.addPredicate(name, description, reflective, transitive, subject, object)
    return "<success></success>"


def processPredicateDefinitionDelete(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    for child in root:
        if child.tag == "name":
            kd.predicateDefinitionManager.deletePredicate(child.text)
            return "<success></success>"
    return "<failed>You have to include a name tag to your query.</failed>"

#
# URIIO TYPE related stuff
#

def processURIIOTypeQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    criteria = kd.typeManager.getCriteria()

    """
    built the criteria object
    """
    for child in root:
        if child.tag == "name":
            ctp = kd.typeManager.getType(child.text)
            if ctp is not None:
                criteria.type = ctp
            for ch in child:
                if ch.tag == "exactType":
                    if ch.text == "yes":
                        criteria.exactType = True

        if child.tag == "properties":
            for aptag in child:
                if aptag.tag == "property":
                    criteria.atomicProperties.append(aptag.text)

    criteria.resolve()

    return criteria.asXML()

def processURIIOCondensedTypeQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    nType = kd.typeManager.getType(root.text)
    print(root.text)
    if nType is None:
        return "<failed>Could not find type " + root.text + " in this Knowledge Domain</failed>"
    cType = nType.condense()
    xmlStr = "<condensedType><name>" + cType.type + "</name>"
    strlocked = "no"
    if nType.locked:
        strlocked = "yes"
    strsysdef = "no"
    if nType.systemDefined:
        strsysdef = "yes"
    xmlStr += "<locked>" + strlocked + "</locked>"
    xmlStr += "<systemDefined>" + strsysdef + "</systemDefined>"
    xmlStr += "<parent>"
    if nType.parent is not None:
         xmlStr += nType.parent.type
    xmlStr += "</parent>"
    xmlStr += "<superTypes>"
    for st in cType.supertypes:
        xmlStr += "<superType>" + st + "</superType>"
    xmlStr += "</superTypes>"
    xmlStr += "<properties>"
    for ap in cType.properties:
        xmlStr += "<property>" + ap.name + "<type>" + ap.type + "</type></property>"
    xmlStr += "</properties>"
    xmlStr += "</condensedType>"

    return xmlStr

def processURIIOBaseTypeQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    nType = kd.typeManager.getType("type")
    xmlStr = "<baseType>"
    xmlStr += "<name>" + nType.type + "</name>"
    xmlStr += "</baseType>"
    return xmlStr

def processURIIOSubTypesQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    nType = kd.typeManager.getType(root.text)
    xmlStr = "<subTypes>"
    for child in nType.children:
        xmlStr += "<subType>" + child.type + "</subType>"
    xmlStr += "</subTypes"
    return xmlStr

def processURIIOTypePurge(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    kd.typeManager.purgeDictionary()
    return kd.typeManager.getCriteria().asXML()

def processURIIOTypeEvolve(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    if kd.typeManager.getType(root.text) is None:
        return "<failed>Passed type does not exist in the type dictionary.</failed>"
    kd.typeManager.evolve(root.text)
    return kd.typeManager.getCriteria().asXML()

def processURIIOTypeDelete(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    if kd.typeManager.getType(root.text) is None:
        return "<failed>type " + root.text + " does not exist in the type dictionary.</failed>"
    kd.typeManager.delete(root.text)
    return kd.typeManager.getCriteria().asXML()

def processURIIOTypeSave(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    for child in root:
        if child.tag == "type":
            nType = URIIOType(None, "")
            for ch in child:
                if ch.tag == "name":
                    nType.type = ch.text
                elif ch.tag == "property":
                    prop = URIIOTypeProperty(ch.text)
                    for c in ch:
                        if c.tag == "type":
                            prop.type = c.text
                    nType.properties.append(prop)
                elif ch.tag == "parent":
                    p = kd.typeManager.getType(ch.text)
                    if p is not None:
                        nType.parent = p
                elif ch.tag == "locked":
                    if ch.text == "yes":
                        nType.locked = True
                    else:
                        nType.locked = False
            kd.typeManager.saveType(nType)

    return kd.typeManager.getCriteria().asXML()

#
# Predicate Related Stuff
#
def processPredicateQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    predname = ""
    for child in root:
        if child.tag == "predicate":
            predname = child.text
    preddef = kd.predicateDefinitionManager.getPredicate(predname)
    if preddef is None:
        return "<failed>The predicate with name '" + predname + "' does not exist in this Knowledge Domain.</failed>"
    list = kd.predicateManager.getPredicatesForPredicateDefinition(preddef)
    output = "<predicates>"
    for p in list:
        output += "<predicate>"
        output += "<subject>" + p.subject.type + "</subject>"
        output += "<predicate>" + p.predicate.name + "</predicate>"
        output += "<object>" + p.object.type + "</object>"
        output += "</predicate>"
    output += "</predicates>"
    return output

def processPredicateURIQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uri = ""
    for child in root:
        if child.tag == "uri":
            uri = child.text
    uriio = kd.URIIOManager.getURIIO(uri)
    if uriio is None:
        return "<failed>The URIIO with URI '" + uri + "' does not exist in this Knowledge Domain.</failed>"
    list = kd.predicateManager.getPredicatesForURIIO(uriio)
    output = "<predicates>"
    for p in list:
        output += "<predicate>"
        output += "<subject>" + p.subject.type + "</subject>"
        output += "<predicate>" + p.predicate.name + "</predicate>"
        output += "<object>" + p.object.type + "</object>"
        output += "</predicate>"
    output += "</predicates>"
    return output

def processAddPredicate(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    suburi = ""
    objuri = ""
    predname = ""
    for child in root:
        if child.tag == "subject":
            suburi = child.text
        elif child.tag == "object":
            objuri = child.text
        elif child.tag == "predicate":
            predname = child.text
    sub = kd.URIIOManager.getURIIO(suburi)
    if sub is None:
        return "<failed>Subject with URI " + suburi + "is not known in this Knowledge Domain</failed>"
    obj = kd.URIIOManager.getURIIO(objuri)
    if obj is None:
        return "<failed>Subject with URI " + objuri + "is not known in this Knowledge Domain</failed>"
    pred = kd.predicateDefinitionManager.getPredicate(predname)
    if pred is None:
        return "<failed>Predicate with name " + predname + " is not known in this Knowledge Domain</failed>"
    kd.predicateManager.addPredicate(sub, pred, obj)

    return "<success></success>"

def processRemovePredicate(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    suburi = ""
    objuri = ""
    predname = ""
    for child in root:
        if child.tag == "subject":
            suburi = child.text
        elif child.tag == "object":
            objuri = child.text
        elif child.tag == "predicate":
            predname = child.text
    sub = kd.URIIOManager.getURIIO(suburi)
    if sub is None:
        return "<failed>Subject with URI " + suburi + "is not known in this Knowledge Domain</failed>"
    obj = kd.URIIOManager.getURIIO(objuri)
    if obj is None:
        return "<failed>Subject with URI " + objuri + "is not known in this Knowledge Domain</failed>"
    pred = kd.predicateDefinitionManager.getPredicate(predname)
    if pred is None:
        return "<failed>Predicate with name " + predname + " is not known in this Knowledge Domain</failed>"
    kd.predicateManager.removePredicate(sub, pred, obj)

    return "<success></success>"

#
# Template Related Stuff
#

def processSaveTemplate(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    for ttype in root:
        if ttype.tag == "XLSXTemplate":
            t = TemplateXLSX()
            for objtempl in ttype:
                odef = XLSXObjectTemplate("type")
                for obchild in objtempl:
                    if obchild.tag == "type":
                       odef.type = obchild.text
                    elif obchild.tag == "property":
                        prop = XLSXObjectPropertyTemplate(0,0,0,0)
                        for p in obchild:
                            if p.tag == "x":
                                prop.x = int(p.text)
                            elif p.tag == "y":
                                prop.y = int(p.text)
                            elif p.tag == "namex":
                                prop.namex = int(p.text)
                            elif p.tag == "namey":
                                prop.namey = int(p.text)
                            elif p.tag == "name":
                                prop.name = p.text
                        odef.properties.append(prop)
                    elif obchild.tag == "connector":
                        conn = XLSXObjectConnectorTemplate(0,0,"type", "", "has relation to", False)
                        for c in obchild:
                            if c.tag == "x":
                                conn.x = int(c.text)
                            elif c.tag == "y":
                                conn.y = int(c.text)
                            elif c.tag == "type":
                                conn.type = c.text
                            elif c.tag == "property":
                                conn.property = c.text
                            elif c.tag == "predicate":
                                conn.predicate = c.text
                            elif c.tag == "subject":
                                sub = True
                                if c.text == "no":
                                    sub = False
                                conn.subject = sub
                        odef.connectors.append(conn)
                t.objectTemplates.append(odef)
            kd.templateManager.setTemplate(t)

    return "<success></success>"

#
# DataSource Related Stuff
#

def processSaveDataSource(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    for dstype in root:
        if dstype.tag == "XLSXSource":
            src = DataSourceXLSX("")
            for ch in dstype:
                if ch.tag == "file":
                    src.sourceFile = ch.text
                elif ch.tag == "template":
                    kdmanager = KnowledgeDomainManager()
                    kd = kdmanager.getDomain()
                    tpt = kd.templateManager.getTemplate(ch.text)
                    if tpt is not None:
                        src.template = tpt
            kd.dataSourceManager.addDataSource(src)

    return "<success></success>"