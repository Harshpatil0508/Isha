password = "Admin"
attempts = 3

while attempts>0:
    userpass = input("Enter the password : ")
    if(userpass==password):
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Invalid password, you have {attempts} chances left")
