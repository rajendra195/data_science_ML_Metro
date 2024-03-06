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
        # return False
        print("user_not exists")
    elif user_exists(username):
        query = """select password from user_detail where username = ? """
        pasw = cur.execute(query, (username,)).fetchall()
        for item in pasw:
            db_pass = list(item)
        
        if bcrypt.checkpw(bytes(password, "utf-8"), db_pass[0]):
            return True
        else:
            return False
        


        # print(username, pasw, db_pass)
def logout():
    def
         
    
def main():
    print(f"Hi! Welcome to the User Authentication and Management System.")
    print(F"What do you want to do? Register/login/update_password/delete_account/")
    desire = input("Enter Register/Login/Update/Delete: ")
    if desire.lower().strip() == "register":
        user_pass = username_password()
        if user_pass != None:
            user_name, password = user_pass
        if not user_exists(user_name) and valid_password(password):
            register_user(username=user_name, password=password)

    elif desire.lower().strip() == "login":
        with open("logged.txt") as file:
            data = file.readlines()
        if len(data) > 0:
            print("User is already logged in!! Please logout first.")

        elif len(data) == 0:    
            user_name = input("Enter a username: ")
            password = input("Enter a password: ")
            if valid_password(password):
                login(username=user_name, password=password)
                try:
                    if not login(username=user_name, password=password):
                        raise InvalidUsernamePassword("Invalid Username or password")
                except InvalidUsernamePassword as e:
                    print(e)
                else:
                    with open("logged.txt", "w") as file:
                        file.write(user_name)
                    # print(user_name)
                    print("Login Successfull!!!")
            else:
                print("Invalid password")

        

        
if __name__ == "__main__":

    main()
    


    # # query = """insert into user_detail(firstname, lastname, username, password, email)
    # #                     values ("Rajendra", "Niroula", "@niorula", "ldkfjdf", "dlkf@dkfl.com")"""
    # # cur.execute(query)
    # query = """delete from user_detail where username = "@niorula" """
    # cur.execute(query)
    # data = cur.execute("select * from user_detail").fetchall()
    # conn.commit()
    # print(data)

    # p1 = hash_password("rajendra")
    # p2 = hash_password("rajendra")
    # print(p1, p2)
