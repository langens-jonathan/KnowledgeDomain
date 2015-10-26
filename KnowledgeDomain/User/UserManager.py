__author__ = 'jeuna'
from KnowledgeDomain.User.UserBox import UserBox
from KnowledgeDomain.KnowledgeInstance import KnowledgeInstance

class UserManager:
    USERBOX = None

    def __init__(self):
        if UserManager.USERBOX is None:
            UserManager.USERBOX = UserBox("jonathan")
            UserManager.USERBOX.resetKnowledgeInstance()


    @classmethod
    def getUserBoxForUser(self, username):
        return UserManager.USERBOX