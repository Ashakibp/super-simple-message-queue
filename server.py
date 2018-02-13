from messageService import messageService
import json
from flask import request, Flask

msgService = messageService()
app = Flask(__name__)


@app.route("/newUser/<firstName>/<lastName>/<email>")
def newUser(firstName, lastName, email):
  msgService.newUser(firstName, lastName, email)
  return True

  
