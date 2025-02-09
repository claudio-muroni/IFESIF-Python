from getpass import getpass

def ask_for_credentials():
    credentials = {}
    credentials["email"] = input("Insert mail -> ")
    credentials["password"] = getpass("Insert pw -> ")
    return credentials