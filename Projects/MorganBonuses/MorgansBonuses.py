multList = [[5, 9, 16, 22, 30],
            [10, 12, 18, 24, 36],
            [20, 25, 32, 42, 53],
            [32, 38, 45, 55, 68],
            [46, 54, 65, 77, 90],
            [60, 72, 84, 96, 120],
            [85, 100, 120, 140, 175]]

while True:
    try:
        weeks = int(input("Insert the number of weeks that you have worked: "))
        if weeks == 999:
            print("Thank you for using this program")
            break
        elif weeks == 0:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            
            if reviewValue == 0:
                print("Bonus: $" + str(multList[0][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[0][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[0][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[0][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[0][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[0][4]))
       
        elif weeks == 1:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue== 0:
                print("Bonus: $" + str(multList[1][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[1][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[1][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[1][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[1][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[1][4]))
       
        elif weeks == 2:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue == 0:
                print("Bonus: $" + str(multList[2][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[2][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[2][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[2][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[2][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[2][4]))
        
        elif weeks == 3:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue == 0:
                print("Bonus: $" + str(multList[3][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[3][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[3][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[3][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[3][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[3][4]))
        
        elif weeks == 4:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue == 0:
                print("Bonus: $" + str(multList[4][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[4][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[4][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[4][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[4][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[4][4]))
       
        elif weeks == 5:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue == 0:
                print("Bonus: $" + str(multList[5][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[5][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[5][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[5][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[5][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[5][4]))
        
        elif weeks == 6:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue == 0:
                print("Bonus: $" + str(multList[6][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[6][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[6][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[6][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[6][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[6][4]))
       
        elif weeks > 6:
            reviewValue = int(input("Insert the number of positive reviews you received: "))
            if reviewValue == 0:
                print("Bonus: $" + str(multList[6][0]))
            elif reviewValue == 1:
                print("Bonus: $" + str(multList[6][1]))
            elif reviewValue == 2:
                print("Bonus: $" + str(multList[6][2]))
            elif reviewValue == 3:
                print("Bonus: $" + str(multList[6][3]))
            elif reviewValue == 4:
                print("Bonus: $" + str(multList[6][4]))
            elif reviewValue > 4:
                print("Bonus: $" + str(multList[6][4]))
    except:
        print("Invalid input.")
