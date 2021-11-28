import requests
import json
import base64
import ast 

_API_domain = "https://api.mojang.com/profiles/minecraft"
_SKIN_domain = "https://sessionserver.mojang.com/session/minecraft/profile/"
def getUUID(username):
    response = requests.post(_API_domain, json=username)
    return response.json()[0]["id"]
#    if not response.ok:
#       return None

def getProfile(uuid):
    url = _SKIN_domain+uuid
    response = requests.get(url)
    value = response.json()["properties"][0]["value"]
    userProfile = ast.literal_eval(base64.b64decode(value).decode())
    return(userProfile)