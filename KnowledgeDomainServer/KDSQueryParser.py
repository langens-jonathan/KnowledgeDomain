__author__ = 'jeuna'
import xml.etree.cElementTree as ET

from KnowledgeDomain.KnowledgeDomainManager import KnowledgeDomainManager
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
    if root.tag == "uriQuery":
        return processURIQuery(root)

    #
    # Predicate Definition related stuff
    #
    elif root.tag == "predicateDefinitionQuery":
        return processPredicateDefinitionQuery(root)

    #
    # URIIO TYPE related stuff
    #
    elif root.tag == "uriioTypeQuery":
        return processURIIOTypeQuery(root)
    elif root.tag == "uriioCondensedTypeQuery":
        return processURIIOCondensedTypeQuery(root)
    elif root.tag == "actionPurge":
        return processURIIOTypePurge(root)

    return "unable to process query of type: " + root.tag + "\nFor more info on queries consult the documentation."


def processURIQuery(root):
    return root.tag

def processPredicateDefinitionQuery(root):
    return root.tag

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
    kd.typeManager.purge()
    return "<actionResult>success</actionResult>"