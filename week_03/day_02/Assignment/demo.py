# import bcrypt
 
# # Declaring our password
# password = b'GeekPassword'
 
# # Adding the salt to password
# salt = bcrypt.gensalt()
# # Hashing the password
# hashed = bcrypt.hashpw(password, salt)
 
# # printing the salt
# print("Salt :")
# print(salt)
 
# # printing the hashed
# print("Hashed")
# print(hashed)

# import bcrypt

# password = b"kathmandu"
# print(type(password))

# salt = bcrypt.gensalt()

# print(salt)
# hashed = bcrypt.hashpw(password, salt)

# print(hashed)

# validate email

# import re

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# email = "test.emaildomain.com"

# if re.fullmatch(regex, email):
#     print("VAlid email")

# else:
#     print("InvalidEmail")

#validate password

pw = "R@m@_f0rtu9e$"

l, u , n, s = 0, 0, 0, 0

if len(pw) > 8:
    for char in pw:

        # check lowercase
        if char.islower():
            l += 1

        # check uppercase
        elif char.isupper():
            u += 1

        # check digit
        elif char.isdigit():
            n += 1
        
        # check special character
        elif char in "@$_":
            s += 1
else:
    print("Password is too short!! length of password must be greater than 8.")
print(l, u, n, s)

if l > 0 and u > 0 and n > 0 and s > 0:
    print("valid password")
else:
    print("Invalid Password")