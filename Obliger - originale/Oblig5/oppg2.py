import json

class UserList:
    def __init__(self, filename: str=None, users: dict={}):
        self.filename = filename

        if filename is not None and users == {}:
            try:
                file = open(filename, "rt")
                users = json.loads(file.read())
                file.close()
            except:
                pass

        self.users = users

    def save_to_json(self):
        try:
            json_string = json.dumps(self.users)

            file = open(self.filename, "wt")
            file.write(json_string)
            file.close()
            return 0
        except:
            return -1

    def append_user(self, full_name: str, suffix: str):
        username = self.__lagBrukernavn(full_name, self.users)
        email = self.__lagEpost(username, suffix)

        self.users[username] = {
            "full name": full_name,
            "email": email
            }
    
    def remove_user(self, username: str):
        removed_user = self.users.pop(username)

        return f'removed {removed_user["full name"]}({username}) from user list'
    
    def skrivUtEposter(self):
        users = self.users

        for user in users:
            print(users[user]["email"])
    
    def __lagBrukernavn(self, full_name: str, user_dict: dict):
        split_name = full_name.lower().split()

        nums_of_letters = 0
        extra_nums = 0
        username = split_name[0] + split_name[1][0]

        duplicate = username in user_dict

        while duplicate is True:
            nums_of_letters += 1

            username = split_name[0] + split_name[1][:+nums_of_letters]

            if nums_of_letters > len(split_name[1]):
                extra_nums += 1
                username = username + str(extra_nums)

            duplicate = username in user_dict

        return username
    
    def __lagEpost(username: str, suffix: str):
        return f'{username}@{suffix}'

def main():
    uio_users = UserList("./UIO_users.json")

    run = True

    while run:
        userin = input("")

        if userin == "i":
            userin_name = input("Skriv det fulle navnet: ")
            userin_suffix = input("Skriv brukerens epost-suffix: ")

            uio_users.append_user(userin_name, userin_suffix)
        elif userin == "r":
            userin_username = input("Skriv brukernavnet til brukeren du vil fjerne: ")

            print(uio_users.remove_user(userin_username))
        elif userin == "p":
            uio_users.skrivUtEposter()
        elif userin == "s":
            run = False

            if uio_users.save_to_json() == -1:
                raise Exception("Failed to save .json file")
            else:
                print(f'saved as {uio_users.filename}')

if __name__ == "__main__":
    main()