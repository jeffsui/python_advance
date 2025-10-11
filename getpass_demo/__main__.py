import getpass

password = getpass.getpass(prompt="Enter your password")

if password == "admin":
    print("Access granted")
else:
    print("Access denied!")