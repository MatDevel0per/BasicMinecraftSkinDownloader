import apiWorker as api
from user import UserProfile



names = []

def main():
    username = input("Enter Minecraft UserName:")
    names.append(username)
    UUID = api.getUUID(names)
    user = api.getProfile(UUID)
    user = UserProfile(user)
    












if __name__ == "__main__":
    main()