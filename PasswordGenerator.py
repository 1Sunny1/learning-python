import random


def GetRandomCharacter():
    return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[{]};:|,.?/')


def GeneratePassword(length):
    combination = []
    for i in range(length):
        character = GetRandomCharacter()
        combination += character
    return combination


passwordLength = int(input("How long do you want to your password be?: "))
while True:
    password = GeneratePassword(passwordLength)
    print("Your new password is:")
    for char in password:
        print(char, end='')
    userChoice = input("\nGenerate again?(type something or \"exit\"): ")
    if userChoice == "exit" or userChoice == "Exit":
        break

print("Bye.\n")


