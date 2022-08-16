import json 

fin = open("Words for Question 1 - Dictionary.json", "r")
cont = json.load(fin)

def findword():
    word = input("Please insert the word you would like to lookup in the dictionary:   ").capitalize()
    found = False 
    for i in cont:
        if i == word:
            found = True 
    if found == False:
        print("Word is not found in the dictionary")
    else:
        print("Found in the dictionary!")

def dispsm():
    word = input("Insert a word that can be searched in the dictionary and display the meaning of:  ").capitalize()
    found = False 
    for key,value in cont.items():
        if key==word or word in value:
            found = True
            print("Word {} - Meaning {}".format(key,value))
    if found == False:
        print("Found word in dictionary")

while True:
    try:
        print("I N T E R A C T I V E   D I C T I O N A R Y ")
        print("=========================================")
        print("1. Search a specific word")
        print("2. Display the word and meaning")
        print("3. Exit")

        choice = int(input("Enter your choice from options 1 to 3):  "))
        if choice == 1:
            findword()
        elif choice == 2:
            dispsm()
        elif choice == 3:
            break
        else:
            print("Invalid number! Enter any number between 1-3:  ")
    except:
        print("Invalid input")



            

 