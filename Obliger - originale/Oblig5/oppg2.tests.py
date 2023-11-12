import oppg2

def test_lagBrukernavn():
    result_username = oppg2.lagBrukernavn("Kari Nordmann")
    expected_username = "karin"

    assert result_username == expected_username, "Expected " + expected_username + ", but got " + result_username

def test_lagEpost():
    result_username = oppg2.lagEpost(oppg2.lagBrukernavn("Kari Nordmann"), "student.matnat.uio.no")
    expected_username = "karin@student.matnat.uio.no"

    assert result_username == expected_username, "Expected " + expected_username + ", but got " + result_username

print("success")