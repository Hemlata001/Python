# Correct username and password
correct_username = "himanshi"
correct_password = "himanshi2004"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Condition checking
if username == correct_username:
    if password == correct_password:
        print("Login successful! Both username and password are correct.")
    else:
        print("Username is correct but password is incorrect.")
else:
    print("Username is incorrect.")
