import apiWorker as api
from user import UserProfile
import configparser


names = []

def main():
    username = input("Enter Minecraft UserName: ")
    names.append(username)
    UUID = api.getUUID(names)
    user = api.getProfile(UUID)
    user = UserProfile(user)
    api.download(user.skin_url, user.name, filePath)





if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("actual.ini")
    guiMode = config['DEFAULT']['GUI']
    filePath = config['DEFAULT']['DownloadLocation']
    main()