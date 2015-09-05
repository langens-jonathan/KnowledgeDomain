__author__ = 'Jonathan Langens'
"""
@author jonathan langens
@created 18/08/2015
@description the URIIOType class is meant to describe types and type hierarchy in an organised way. In some respect it c
an be thought of as just a taxonomy. But it also adds properties and 3 operations that are beyond basics:
(1) condense:
when a type condenses it just throws all information about it in 1 condensed type form (you can think of this as what wo
uld be found in an encyclopedia)
(2) evolve:
the type creates a sibling and gives it back to the caller of the function. This can be used efficiently if types are di
scovered that need extra properties or less.
(3) purge:
when a type purges it checks it children to see if they share properties. If all children share a property then this pro
perty belongs to the parent type. If some children share properties then an in between type needs to be added.
"""
class URIIOType:

    """
    @param parent if this type is the base type of which all other types are subtypes then parent is none, otherwise the
    parent parameter is itself also a URIIOType
    @param type a string representation of the name of the type
    @pre the parent has to be initialised if isnt None and the name should be unique to this type
    @post a fully initialized type
    """
    def __init__(self, parent, type):
        self.children = []
        self.parent = parent
        if parent is not None:
            self.parent.children.append(self)
        self.type = type
        self.typeProperties = []# these are other types which are properties of this type
        self.atomicProperties = []# these are just strings
        self.locked = False# human users can set a type to locked if they are sure that it is definite
        self.systemDefined = False#A system defined type cannot be altered

    """
    @description this returns a list of all the types this type is (ie if the type is dog its also mamal, creature,...)
    @return a list of type this type is
    """
    def asTypeList(self):
        list = []
        if self.parent != None:
            list.extend(self.parent.asTypeList())
        list.append(self.type)
        return list

    """
    @description returns a list that represents all types that are a part of this type
    """
    def asTypePropertyList(self):
        list = []
        if self.parent != None:
            list.extend(self.parent.asTypePropertyList())
        list.extend(self.typeProperties)
        return list

    """
    @description returns all properties this type has and all properties of all of its parent
    """
    def asAtomicPropertyList(self):
        list = []
        if self.parent != None:
            list.extend(self.parent.asAtomicPropertyList())
        list.extend(self.atomicProperties)
        return list

    """
    @para type the typename
    @return True if this type is the passed typename or a subtype of a type with this typename
    """
    def isOfType(self, type):
        if self.type == type:
            return True
        if self.parent is not None:
            return self.parent.isOfType(type)
        return False

    """
    @param atomicProperty the name of the property we want to check this type has
    @return True
    """
    def hasAtomicProperty(self, atomicProperty):
        if self.atomicProperties.count(atomicProperty) > 0:
            return True
        if self.parent is not None:
            return self.parent.hasAtomicProperty(atomicProperty)
        return False

    def hasTypeProperty(self, typeProperty):
        if self.typeProperties.count(typeProperty) > 0:
            return True
        if self.parent is not None:
            return self.parent.hasTypeProperty(typeProperty)
        return False

    def getSiblings(self):
        siblings = self.parent.children.copy
        siblings.remove(self)
        return siblings

    """

    """
    def condense(self):
        supertypes = self.asTypeList()
        supertypes.remove(self.type)
        typelist = self.asTypePropertyList()
        atomlist = self.asAtomicPropertyList()
        condesed = URIIOCondensedType(self.type, supertypes, typelist, atomlist)
        return condesed

    def evolve(self):
        parent = self.parent
        if len(self.children) > 0:
            parent = self
        evolution = URIIOType(parent, self.type + "x")
        evolution.typeProperties = self.typeProperties.copy()
        evolution.atomicProperties = self.atomicProperties.copy()
        return evolution

    def purge(self):
        # if this type is locked we only pass the purge to its children
        if self.locked:
            for child in self.children:
                child.purge()
                return

        # first remove all properties that already appear in parents
        for child in self.children:
            tprops = []
            for typeprop in child.typeProperties:
                if self.hasTypeProperty(typeprop):
                    tprops.append(typeprop)

            for typeprop in tprops:
                child.typeProperties.remove(typeprop)

            aprops = []
            for atomprop in child.atomicProperties:
                if self.hasAtomicProperty(atomprop):
                    aprops.append(atomprop)

            for atomprop in aprops:
                child.atomicProperties.remove(atomprop)

        for child in self.children:
            for typeprop in child.typeProperties:
                occuranceList = []
                for child in self.children:
                    if child.typeProperties.count(typeprop):
                        occuranceList.append(child)
                if len(occuranceList) ==  len(self.children) and len(self.children) > 1:
                    self.__extractFromChildren(typeprop, None)
                else:
                    if len(occuranceList) > 2 and len(occuranceList) > len(self.children) * 0.75:
                        self.__createSubtypeForProperty(occuranceList)
                occuranceList.clear()

            for atomprop in child.atomicProperties:
                occuranceList2 = []
                for child in self.children:
                    if child.atomicProperties.count(atomprop):
                        occuranceList2.append(child)
                if len(occuranceList2) ==  len(self.children) and len(self.children) > 1:
                    self.__extractFromChildren(None, atomprop)
                else:
                    if len(occuranceList2) > 2 and len(occuranceList2) > len(self.children) * 0.75:
                        self.__createSubtypeForProperty(occuranceList2)
                occuranceList2.clear()

        for child in self.children:
            child.purge()

    # helper function that extracts a property from all children of a type and injects it into the supertype
    def __extractFromChildren(self, typeProperty, atomicProperty):
        if typeProperty is not None:
            self.typeProperties.append(typeProperty)
            for child in self.children:
                child.typeProperties.remove(typeProperty)

        if atomicProperty is not None:
            self.atomicProperties.append(atomicProperty)
            for child in self.children:
                child.atomicProperties.remove(atomicProperty)

    # helper function that defines that a subgroup of children from a type will fall under a new subclass of that type
    def __createSubtypeForProperty(self, listOfChildren):
        newType = URIIOType(self, self.type + "0")
        for child in listOfChildren:
            self.children.remove(child)
            child.parent = newType
        newType.children = listOfChildren

"""
a condensed type is just an 'instantiation' of a type, it will return an object that knows
its supertypes and has all properties it needs to have
you can think of a
"""
class URIIOCondensedType:
    def __init__(self, type, supertypes, typeProperties, atomicProperties):
        self.type = type
        self.supertypes = supertypes
        # we want the type properties to be condensed in this case as well
        self.typeProperties = []
        for uriiotype in typeProperties:
            self.typeProperties.append(uriiotype.asCondensedType)
        self.atomicProperties = atomicProperties

    def isOfType(self, type):
        if self.type == type:
            return True
        for t in self.supertypes:
            if t == type:
                return True
        return False

    def hasAtomicProperty(self, prop):
        for ap in self.atomicProperties:
            if ap == prop:
                return True
        return False

    def hasTypeProperty(self, prop):
        for tp in self.typeProperties:
            if tp.isOfType(prop.type):
                return True
        return False

    def print(self):
        print("type: " + self.type)
        print("| supertypes: ")
        for st in self.supertypes:
            print("| - " + st)
        print("|")
        print("| properties:")
        for ap in self.atomicProperties:
            print("| * " + ap)
        for tp in self.typeProperties:
            print("| @ " + tp.type)