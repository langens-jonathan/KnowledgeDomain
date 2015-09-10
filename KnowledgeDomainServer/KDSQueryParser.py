__author__ = 'jeuna'
import xml.etree.cElementTree as ET

from KnowledgeDomain.KnowledgeDomainManager import KnowledgeDomainManager
from KnowledgeDomain.URIIOType import URIIOType
"""
from KnowledgeDomain.URIIOCriteria import URIIOCriteria
from KnowledgeDomain.URIIOTypeCriteria import URIIOTypeCriteria
from KnowledgeDomain.URIIOPredicateDefinitionCriteria import URIIOPredicateDefinitionCriteria
"""
def ParseQuery(query):
    root = ET.fromstring(query)

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
    elif root.tag == "actionURIIOAddPredicate":
        return processURIIOAddPredicate(root)
    elif root.tag == "actionURIIORemovePredicate":
        return processURIIORemovePredicate(root)


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
    elif root.tag == "actionURIIOTypePurge":
        return processURIIOTypePurge(root)
    elif root.tag == "actionURIIOTypeEvolve":
        return processURIIOTypeEvolve(root)
    elif root.tag == "actionURIIOTypeDelete":
        return processURIIOTypeDelete(root)
    elif root.tag == "actionURIIOTypeSave":
        return processURIIOTypeSave(root)

    return "unable to process query of type: " + root.tag + "\nFor more info on queries consult the documentation."

#
# URIIO Related stuff
#

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


def processURIIONew(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    uriio = kd.URIIOManager.newURIIO()
    return uriio.asXML()

def processURIIODelete(root):
    return root.tag

def processURIIOAddProperty(root):
    return root.tag

def processURIIORemoveProperty(root):
    return root.tag

def processURIIOAddPredicate(root):
    return root.tag

def processURIIORemovePredicate(root):
    return root.tag

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
    return root.tag

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

        if child.tag == "atomicProperties":
            for aptag in child:
                if aptag.tag == "atomicProperty":
                    criteria.atomicProperties.append(aptag.text)

    criteria.resolve()

    return criteria.asXML()

def processURIIOCondensedTypeQuery(root):
    kdmanager = KnowledgeDomainManager()
    kd = kdmanager.getDomain()
    nType = kd.typeManager.getType(root.text)
    print(root.text)
    cType = nType.condense()
    xmlStr = "<condensedType><name>" + cType.type + "</name>"
    xmlStr += "<superTypes>"
    for st in cType.supertypes:
        xmlStr += "<superType>" + st + "</superType>"
    xmlStr += "</superTypes>"
    xmlStr += "<atomicProperties>"
    for ap in cType.atomicProperties:
        xmlStr += "<atomicProperty>" + ap + "</atomicProperty>"
    xmlStr += "</atomicProperties>"
    xmlStr += "</condensedType>"

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
        return "<failed>type " + root.text + " does not exist in the type dictionary.</failed>"
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
                elif ch.tag == "typeProperty":
                    tp = kd.typeManager.getType(ch.text)
                    if tp is not None:
                        nType.typeProperties.append(tp)
                elif ch.tag == "atomicProperty":
                    nType.atomicProperties.append(ch.text)
                elif ch.tag == "parent":
                    p = kd.typeManager.getType(ch.text)
                    if p is not None:
                        nType.parent = p
                elif ch.tag == "locked":
                    if ch.text == "true":
                        nType.locked = True
                    else:
                        nType.locked = False
            kd.typeManager.saveType(nType)

    return kd.typeManager.getCriteria().asXML()