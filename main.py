import random
def generateNickname(nickname): 
    print(f'{name[0]} "{nickname}" {name[1]}')

def changeName():
    firstName = input("please enter first name: ")
    lastName = input("please enter last name: ")
    name[0] = firstName
    name[1] = lastName
    print(f"Name has been changed to {firstName} {lastName}")

def addNickname():
    newNickname = input("Enter new name: ")
    if(newNickname not in nicknameList):
        nicknameList.append(newNickname)
        print("Success! nickname added")
    else:
        print("nickname already added")

def removeNickname():
    nicknamerm = input("Enter nickname to remove: ")
    if(nicknamerm in nicknameList):
        nicknameList.remove(nicknamerm)
        print("success! nickname removed")
    else:
        print("nickname not found")


nicknameList = ["Crusher", "the Scientist", "Twinkle-toes", "The Coder", "the Jester", "the Sloth", "Quick-Silver"]
name = ["Fistname", "Lastname"]


exit = False
loop = 1
while(not exit):
    if(loop == 1):
        changeName()
    print(f"MAIN MENU ({name[0]} {name[1]})")
    print("SELECT AN OPTION")
    print("1: Change Name")
    print("2: Display a Random Nickname")
    print("3: Display All Nicknames")
    print("4: Add a Nickname")
    print("5: Remove a Nickname")
    print("6: Exit")
    option = int(input())

    if(option == 1):
        changeName()
    elif(option == 2):
        generateNickname(nicknameList[random.randint(0, len(nicknameList) - 1)])
    elif(option == 3):
        for i in nicknameList:
            generateNickname(i)
    elif(option == 4):
        addNickname()
    elif(option == 5):
        removeNickname()
    elif(option == 6): 
        exit = True
    loop+=1