

userBase = [['John',['password', '123','swordfish']],['Jack',['apple', 'peach','banana']]]



def userChecks():
    userName = input("Type in username: ")



    newPass = True
    userCheck = False

    for i in range(0, len(userBase)):
        if(userBase[i][0]==userName):
            userCheck = True
            newPassword = input("Type in new password: ")
            for j in range(0, len(userBase[i][1])):
                if(userBase[i][1][j]==newPassword):
                    print("You have used this password before")
                    newPass = False
                else:
                    print("No match.")
            if(newPass==True):
                userBase[i][1].append(newPassword)
                print("New password added")
                print(userBase)

    if(userCheck==False):
        print("Username not recognized.")
        userChecks()

userChecks()
