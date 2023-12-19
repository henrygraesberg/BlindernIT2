import json, os

class UserList:
    def __init__(self, filename: str=None, users: dict={}) -> None:
        """
        Initiates a UserList object

        Args:
            filename (str, optional): Directory of the file where users will be saved upon calling save_to_json(). Defaults to None.
            users (dict, optional): Dictionary of users. Defaults to {}.
            !IMPORTANT If users is not an empty dict and filename is not None, users will overwrite the content of filename upon calling save_to_json()
        """
        self.filename = filename

        if filename is not None and users == {}:
            try:
                file = open(filename, "rt")
                users = json.loads(file.read())
                file.close()
            except:
                pass

        self.users = users

    def __str__(self) -> str:
        output = "\n"
        
        for i in self.users:
            output += self.users[i]["email"] + "\n"
        
        return output

    def save_to_json(self) -> int:
        """
        Saves self.users as a .json string to the directory specified 
        in self.filname

        Returns:
            int: 0 on success, -1 on failiure
        """
        try:
            file = open(self.filename, "wt")
            json_string = json.dumps(self.users, indent=4, sort_keys=True)

            file.write(json_string)
            file.close()
            return 0
        except:
            return -1

    def append_user(self, full_name: str, suffix: str) -> None:
        """
        Adds a user to self.users

        Args:
            full_name (str): Full name of the user to be added
            suffix (str): email suffix of the user to be added
        """
        username = self.__lagBrukernavn(full_name)
        email = self.__lagEpost(username, suffix)

        self.users[username] = {
            "full name": full_name,
            "email": email
            }
    
    def remove_user(self, username: str) -> str:
        """
        removes a user from self.users

        Args:
            username (str): Username of the user to be removed

        Returns:
            str: returns a string explaining success or failure
        """
        try:
            removed_user = self.users.pop(username)

            return f'removed {removed_user["full name"]}({username}) from user list'
        except KeyError:
            return f'could not find {username} in user list'
        except:
            return f'could not remove {username} from user list'

    
    def __lagBrukernavn(self, full_name: str) -> str:
        """
        Makes a unique username based on the full name of the user

        Args:
            full_name (str): Full name of the user

        Returns:
            str: A unique username
        """
        split_name = full_name.lower().split()

        nums_of_letters = 0
        extra_nums = 0
        username = split_name[0] + split_name[1][0]

        duplicate = username in self.users

        while duplicate is True:
            nums_of_letters += 1

            username = split_name[0] + split_name[1][:+nums_of_letters]

            if nums_of_letters > len(split_name[1]):
                extra_nums += 1
                username += str(extra_nums)

            duplicate = username in self.users

        return username
    
    def __lagEpost(self, username: str, suffix: str) -> str:
        """
        Makes an email for the user with the username as a prefix and 
        the supplied suffix as the email domain

        Args:
            username (str): Users username
            suffix (str): Email domain

        Returns:
            str: Email address of the user
        """
        return f'{username}@{suffix}'

def main() -> None:
    uio_users = UserList("./UIO_users.json")

    run = True

    while run is True:
        userin = input("")

        if userin == "i":
            userin_name = input("Skriv det fulle navnet: ")
            userin_suffix = input("Skriv brukerens epost-suffix: ")

            uio_users.append_user(userin_name, userin_suffix)
        elif userin == "r":
            userin_username = input("Skriv brukernavnet til brukeren du vil fjerne: ")

            print(uio_users.remove_user(userin_username))
        elif userin == "p":
            print(uio_users)
        elif userin == "s":
            run = False

            if uio_users.save_to_json() == -1:
                raise FileExistsError("Failed to save .json file")
            else:
                print(f'saved as {uio_users.filename}')
        elif userin == "d":
            confirmation = input("This action will delete both the json file and the current user list being worked on and stop the program. Are you sure? y/n: ")

            if confirmation == "y":
                os.remove(uio_users.filename)
                uio_users.users = {}

                run = False

if __name__ == "__main__":
    main()
    