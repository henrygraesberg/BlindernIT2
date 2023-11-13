import oppg2

def test_lagBrukernavn():
    result_username = oppg2.lagBrukernavn("Kari Nordmann", {})
    expected_username = "karin"

    assert result_username == expected_username, "Expected " + expected_username + ", but got " + result_username

def test_lagEpost():
    result_username = oppg2.lagEpost(oppg2.lagBrukernavn("Kari Nordmann", {}), "student.matnat.uio.no")
    expected_username = "karin@student.matnat.uio.no"

    assert result_username == expected_username, "Expected " + expected_username + ", but got " + result_username

def test_user_list():
    result_UserList = oppg2.UserList()
    result_users_unwrapped = [result_UserList.filename, result_UserList.users]
    expected_users = [None, {}]

    assert result_users_unwrapped == expected_users, f'Expected {expected_users}, but got {result_users_unwrapped}'

test_lagBrukernavn()
test_lagEpost()
test_user_list()

print("success")