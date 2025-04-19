from login import login_page    

def test_login():
    assert login_page("ammu","56789","12345") == "login successful of the user ammu"
    assert login_page("ammu","56789","56789") == "retype password"

if __name__ == "__main__":
    test_login()
    print("All tests passed!")
