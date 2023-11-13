import oppg2

def test_append_user():
    test_obj = oppg2.UserList()
    test_obj.append_user("Kari Nordmann", "student.matnat.uio.no")

    expected_username = "karin"
    expected_email = "karin@student.matnat.uio.no"

    result_username = list(test_obj.users.keys())[0]
    result_email = test_obj.users[expected_username]["email"]
    
    assert result_username == expected_username, "Expected " + expected_username + ", but got " + result_username
    assert result_email == expected_email, "Expected " + expected_email + ", but got " + result_email

def test_user_list():
    result_UserList = oppg2.UserList()
    result_users_unwrapped = [result_UserList.filename, result_UserList.users]
    expected_users = [None, {}]

    assert result_users_unwrapped == expected_users, f'Expected {expected_users}, but got {result_users_unwrapped}'

test_user_list()
test_append_user()

print("success")