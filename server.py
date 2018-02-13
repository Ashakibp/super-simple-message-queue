from messageService import messageService
import json
from flask import request, Flask, jsonify

msgService = messageService()
app = Flask(__name__)

@app.route("/newUser/<firstName>/<lastName>/<email>")
def newUser(firstName, lastName, email):
  msgService.newUser(firstName, lastName, email)
  return "Nice"

@app.route("/sendMessage/<email>/<sender>/<reciever>/<text>")
def sendMessage(email, sender, reciever, text):
    msgService.sendMessage(email, sender, reciever, text)
    return "SENT"

@app.route("/getMessages/<email>")
def getMessages(email):
    return jsonify({
        email: msgService.getUser(email).messages
    })





app.run(host='0.0.0.0')