__author__ = 'jeuna'

class Template:
    # all template methods are identified by a hash code. this code can be send to clients to check
    # if they have files that might be read the template
    def getHashCode(self):
        return "noHash"
