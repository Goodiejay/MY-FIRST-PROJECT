import time
# user create a password and try login with the same password created.
attempts=6  #user have 6 trial attepmt 
print("welcome to clipra","to get started")
new_password=input("create a new password: ")
print("password created succesfully")

#loop through
while True:

    attempts_left=0 
    passord=input("Enter password to continue: ") 
    while attempts_left < attempts:
        #checks if the currnt user input matches with the original (new)password
        if passord == new_password: 
            print("correct password")
            exit() #stops the whole loop 
        else:
            attempts_left += 1 
            if attempts_left < attempts:
                print("incorrect password")
                if attempts_left >= 3:
                    print("you have", attempts - attempts_left, "attempts left") 
                passord=input("Try again: ")    
            else:
                print("too many failed attempts"); print("try again after 30 sec")
                time.sleep(30) # login freezes for the given time
                # it starts all over again
                print("you can now try again")
                
