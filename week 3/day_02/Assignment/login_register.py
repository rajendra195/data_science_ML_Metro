import sqlite3
import re
import bcrypt


db_name = "user_data.db"

conn = sqlite3.connect(db_name)
cur = conn.cursor()

class Error(Exception):
    pass

class UserExistsError(Error):
    pass

class InvalidPasswordError(Error):
    pass

class InvalidEmail(Error):
    pass

class InvalidUsernamePassword(Error):
    pass

# creating a table

query = """create table user_detail(firstname varchar[50], 
            lastname varchar[50], username varchar[50], password varchar[50], email varchar[50])"""
# cur.execute(query)

# function to validate password
def valid_password(password):
    l, u, n, s = 0, 0, 0, 0
    if len(password) > 8:
        for char in password:
            if char.islower():
                l += 1
            elif char.isupper():
                u += 1
            elif char.isdigit():
                n += 1
            elif char in "@$_":
                s += 1
            
    if len(password) < 9:
        return False
    elif l > 0 and u > 0 and n > 0 and s > 0 and len(password) > 8:
        return True
    else:
        return False

# function to check user is login or not
def user_logged_in():
    with open("logged.txt", "r") as file:
        data = file.readlines()
    if len(data) > 0:
        return True
    elif len(data) == 0:
        return False

# function to logout user
def log_out_user():
    with open("logged.txt", "w") as file:
        file.write("")

# function to give username of logged in user
def logged_in_username():
    with open("logged.txt", "r") as file:
        user = file.readlines()
        return user[0]

    
# function to check if user entered password and database password is same
def check_password(username, password):
    query = """select password from user_detail where username = ? """
    pasw = cur.execute(query, (username,)).fetchall()
    for item in pasw:
        db_pass = list(item)
        
    if bcrypt.checkpw(bytes(password, "utf-8"), db_pass[0]):
        return True
    else:
        return False


# function to validate email    
def valid_email(email):

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        return True
    else:
        return False

# function to hash password
def hash_password(password):
    hashed_password = bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())
    return hashed_password

# function to check if the user exists in the database or not
def user_exists(username):
    all_db_usernames = cur.execute("select username from user_detail").fetchall()
    # all_db_usernames = [("sldf", ), ("df", )]
    db_usernames = []
    for data in all_db_usernames:
        db_usernames.append("".join(list(data)))
    if username in db_usernames:
        return True
    else:
        return False
    
# function to input username_and password
def username_password():
    user_name = input("Enter a user_name: ")
    try:
        if user_exists(user_name):
            raise UserExistsError("Username already exists!! Please choose another username.") 
    except UserExistsError as e:
        print(e)
        return None

    password = input("Enter a password: ")
    try:
        if not valid_password(password):
            raise InvalidPasswordError("Invalid Password!!Length of password must be greater than 8.\nPassword must contain atleast one uppercase(A-Z), one lowercase(a-z), one special character(@$_) and one digit(0-9)")
    except InvalidPasswordError as e:
        print(e)
        return None
    else:
        return user_name, password


# function to register user
def register_user(username, password):
    hashed_password = hash_password(password)
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter Email: ")
    try:
        if not valid_email(email=email):
            raise InvalidEmail("Invalid Email address!!!")
    except InvalidEmail as e:
        print(e)
    else:
        data_to_insert = (first_name.title(), last_name.title(), username, hashed_password, email)
        query = """insert into user_detail(firstname, lastname, username, password, email)
                    values (?, ?, ?, ?, ?)"""
        cur.execute(query, data_to_insert)
        conn.commit()
        print("User registered Successfully!!!")
    
# function to login user
def login(username, password):
    if not user_exists(username):
        return False
    
    # check if the user is exists in database or not
    elif user_exists(username):

        # check if the user entered password match with the database password or not
        if check_password(username=username, password=password):
            return True
        else:
            return False
        

# function to update password 
def update_password(username, old_password, new_password):
    new_hashed_password = hash_password(new_password)
    # print(new_password, new_hashed_password)
    query = """update user_detail set password = ? where username = ?"""
    cur.execute(query, (new_hashed_password, username))
    conn.commit()
    log_out_user()
    print("Password Update successfull!!!")


# function to delete account
def delete_account(username, password):
    query = "delete from user_detail where username = ? "
    cur.execute(query, (username, ))
    conn.commit()
    log_out_user()
    print("Your account is deleted successfully!!1")

   
def main():
    print(f"Hi! Welcome to the User Authentication and Management System.")
    print(F"What do you want to do? Register/login/update_password/delete_account/")
    desire = input("Enter Register/Login/Update/Delete: ")
    if desire.lower().strip() == "register":

        user_pass = username_password()
        # username_passowrd function return user_name and password
        if user_pass != None:
            user_name, password = user_pass

            # check if user exists and password is valid 
            if not user_exists(user_name) and valid_password(password):
                # register the new user
                register_user(username=user_name, password=password)

    elif desire.lower().strip() == "login":

        # checks if the user is already logged in
        if user_logged_in():
            print("User is already logged in!! Please logout first.")
            log_in = True
            while log_in:
                logout = input("Enter 'logout' to log out: ")
                if logout == "logout":
                    log_out_user()
                    print("User logout successfull!! Re-run the program to login again.")
                    log_in = False
                else:
                    print(f"Incorrect! Please enter 'logout': ")

        # if user is not logged in 
        else:    
            user_name = input("Enter a username: ")
            password = input("Enter a password: ")
            if valid_password(password):
                # function to check whether the username and password is true or not
                login(username=user_name, password=password)
                try:
                    # 
                    if not login(username=user_name, password=password):
                        raise InvalidUsernamePassword("Invalid Username or password.")
                except InvalidUsernamePassword as e:
                    print(e)
                else:
                    with open("logged.txt", "w") as file:
                        file.write(user_name)
                    # print(user_name)
                    print("Login Successfull!!!")
            else:
                print("""Invalid Password!!Length of password must be greater than 8.\nPassword must contain atleast one uppercase(A-Z), one lowercase(a-z), one special character(@$_) and one digit(0-9)""")

    elif desire.strip().lower() == "update":
        if user_logged_in():
            print(f"Hello!! {logged_in_username()}")
            print("Update your password!!")
            user_name = input("Enter your username: ")
            old_psw = input("Enter your old password: ")
            try:
                if user_exists(user_name) and check_password(user_name, old_psw) and logged_in_username() == user_name:
                    new_psw = input("Enter new password: ")
                    if valid_password(new_psw):
                        update_password(username=user_name, old_password=old_psw, new_password=new_psw)
                    else:
                        print("""Invalid New Password!!Length of password must be greater than 8.\nPassword must contain atleast one uppercase(A-Z), one lowercase(a-z), one special character(@$_) and one digit(0-9)""")

                else:
                    raise InvalidUsernamePassword("Email or Password doesn't match.")
            except InvalidUsernamePassword as e:
                print(e)
            

        elif not user_logged_in():
            print(f"User is not logged in!!! Please Login to update password.")

    elif desire.strip().lower() == "delete":
        if user_logged_in():
            print(f"Hello!! {logged_in_username()}")
            print("Are you sure want to delete your account!!")
            user_name = input("Enter your username: ")
            password = input("Enter your old password: ")
            try:
                if user_exists(user_name) and check_password(user_name, password) and logged_in_username() == user_name:
                        delete_account(username=user_name, password=password)
        
                else:
                    raise InvalidUsernamePassword("Email or Password doesn't match.")
            except InvalidUsernamePassword as e:
                print(e)
        else:
            print("User must be logged in to delete an account. Login in.")




        

        
if __name__ == "__main__":

    main()
    


    # # query = """insert into user_detail(firstname, lastname, username, password, email)
    # #                     values ("Rajendra", "Niroula", "@niorula", "ldkfjdf", "dlkf@dkfl.com")"""
    # # cur.execute(query)
    # query = """delete from user_detail where username = "@dube" """
    # cur.execute(query)
    # data = cur.execute("select * from user_detail").fetchall()
    # conn.commit()
    # print(data)

    # p1 = hash_password("rajendra")
    # p2 = hash_password("rajendra")
    # print(p1, p2)
