import random
def generateNickname(nickname): 
    print(f'{name[0]} "{nickname}" {name[1]}')

nicknameList = ["Crusher", "the Scientist", "Twinkle-toes", "The Coder", "the Jester", "the Sloth", "Quick-Silver"]
name = ["Fistname", "Lastname"]


exit = False
while(not exit):
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
        firstName = input("please enter first name: ")
        lastName = input("please enter last name: ")
        name[0] = firstName
        name[1] = lastName
        print(f"Name has been changed to {firstName, lastName}")
    elif(option == 2):
        generateNickname(nicknameList[random.randint(0, len(nicknameList) - 1)])
    elif(option == 3):
        for i in nicknameList:
            generateNickname(i)
    elif(option == 4):
        newNickname = input("Enter new name: ")
        nicknameList.append(newNickname)
    elif(option == 5):
        nicknamerm = input("Enter nickname to remove: ")
        valid = False
        for i in nicknameList:
            if(nicknamerm == i):
                valid = True
        if(valid):
            nicknameList.remove(nicknamerm)
            print("success! nickname removed")
        else:
            print("nickname not found")
    elif(option == 6): 
        exit = True