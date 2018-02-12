from user import User



class messageService:

    def __init__(self):
        self.users = []


    def newUser(self, firstName, lastName, email):
        self.users.append(User(firstName, lastName, email))

    def sendMessage(self, email, sender, reciever, text):
        userMess = message(sender, reciever, text)
        toRecieve = self.getUser(email)
        if(toRecieve == None):
            return False
        toRecieve.messages.append(userMess)


    def getUser(self, emailAddr):
        for user in self.users:
            if user.email == emailAddr:
                return user
        return None




class message:
    def __init__(self, sender, reciever, text):
        self.sender = sender
        self.reciever = reciever
        self.message = text



    def __str__(self):
        return "Dear %s, \n %s \n sincerely, \n %s", self.sender, self.message, self.reciever




x = messageService()
x.newUser("Aaron", "Shakib", "aaronshakib@gmail.com")
print(x.getUser("aaronshakib@gmail.com"))
