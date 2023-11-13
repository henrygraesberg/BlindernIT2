import json

class UserList:
    def __init__(self, filename=None, users: dict={}):
        self.filename = filename

        if filename is not None and users == {}:
            try:
                file = open(filename, "rt")
                users = json.loads(file.read())
                file.close()
            except:
                pass

        self.users = users

    def to_json(self):
        json_string = json.dumps(self.users)

        file = open(self.filename, "wt")
        file.write(json_string)
        file.close()

    def append_user(self, full_name: str, suffix: str):
        username = lagBrukernavn(full_name, self.users)
        email = lagEpost(username, suffix)

        self.users[username] = {
            "full name": full_name,
            "email": email
            }

def lagBrukernavn(full_name: str, user_dict: dict):
    split_name = full_name.lower().split()

    nums_of_letters = 0
    extra_nums = 0
    username = split_name[0] + split_name[1][0]

    duplicate = check_duplicate(username, user_dict)

    while duplicate is True:
        nums_of_letters += 1
        if nums_of_letters > len(split_name[1]):
            extra_nums += 1

        username = split_name[0] + split_name[1][:+nums_of_letters]
        if extra_nums > 0:
            username = username + str(extra_nums)

        duplicate = check_duplicate(username, user_dict)

    return username

def check_duplicate(username: str, user_dict: dict):
    for i in user_dict:
        if i == username:
            return True
    
    return False

def lagEpost(username: str, suffix: str):
    return f'{username}@{suffix}'

def skrivUtEposter(user_list: UserList):
    users = user_list.users

    for user in users:
        print(users[user]["email"])

def main():
    uio_users = UserList("./UIO_users.json")

    run = True

    while run:
        userin = input("")

        if(userin == "i"):
            userin_name = input("Skriv det fulle navnet: ")
            userin_suffix = input("Skriv brukerens epost-suffix: ")

            uio_users.append_user(userin_name, userin_suffix)
        elif(userin == "p"):
            skrivUtEposter(uio_users)
        elif(userin == "s"):
            run = False

            uio_users.to_json()

if __name__ == "__main__":
    main()