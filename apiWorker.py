import requests
import json
import base64
import ast 
import os
from pathlib import Path
import shutil

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

def download(url, username, filepath):
    filename: Path = Path(username + ".jpg")
    pathfile: Path = Path(filepath)
    pathCheck = pathfile / filename
    choice = input(f"The skin will be save at the following location {pathCheck} \nIf this is correct enter yes else enter no: ").lower()
    if choice == "yes":
        # Opens a file with wb ( write binary ) permission.
        with open(pathfile / filename, 'wb') as handle:
            response = requests.get(url, stream=True)

            if not response.ok:
                print(response)
            print("Downloading Skin")
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, handle)
            print("Image Downloaded")
        return
    else:
        print("Option not recognized returning")
        return