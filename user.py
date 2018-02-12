'This is our super easy to use User Template'

class User:

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.messages = []

    def getMessages(self):
        return self.messages


    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName
