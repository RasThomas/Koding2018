#reading a file

def readMyDataFile(dateFile):
    with open(dateFile, mode ='r') as myDataFile:
        item = myDataFile.read().splitlines()
        print(type(item))
        print(item)
        return item


readMyDataFile("someData.txt")

def writeMyDataFile(moreClubs):
    with open("moreData.txt", mode='w') as myDataFile:
        for club in moreClubs:
            myDataFile.write(club+'\n')
        print (moreClubs)

moreClubs =["Ajax", "Bremen"]

writeMyDataFile(moreClubs)

def seeIfItemExists(myItem):
    items = readMyDataFile("someData.txt")
    for item in items:
        if(item == myItem):
            print(myItem, " in the list already.")
            return

    print(myItem, " was not in the list.")
    items.append(myItem)
    writeMyDataFile(items)
    print("Made new list with ", myItem)

seeIfItemExists("Liverpool")

seeIfItemExists("Ajax")


#Fix this
def checkPassword(userName):
    data = readMyDataFile("UserCredentials.txt")
    print(data)
    for user in data:
        userCred = user.split(';')
        print(userCred[0])
        if(userCred[0] == userName):
            print("User found.")
            print("Type password for", userName)
            userPass = input()
            if(userPass == userCred[1]):
                print("Password is correct")
                break
            else:
                print("Password is incorrect")
        else:
            print("User not found.")


checkPassword("Dinesh")