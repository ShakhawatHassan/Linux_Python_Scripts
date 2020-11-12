## Creating and managing user accounts
#Creating an user
import os
import subprocess
import sys
import getpass

def delete_user():
    username = input("Enter Username : ")
    
    try:
        output = subprocess.run(['userdel', usrname ])
        if output.returncode == 0:
            print("User successfully deleted")
    except:
        print(f"Failed to delete your given user")
        sys.exit(1)
delete_user()