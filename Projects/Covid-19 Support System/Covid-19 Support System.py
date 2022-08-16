SA = 3_717_067
USA = 80_019_128
China = 485_204_991

while True:
        Choice = 0
        print("Welcome to the COVID 19 support service. Please select an option below:")
        print("1.Statistics", "\n2.Prevention", "\n3.Symptoms", "\n4.Treatment", "\n5.Report case", "\n6.Exit")
        print("Ënter choice(1/2/3/4/5/6): ")

        Choice = input()
        if Choice == "1":

            print("\nCurrently in SA there are 3_717_067 confirmed cases")
            print("Currently in USA there are 80_019_128 confirmed cases")
            print("Currently in China there are 485_204_991 confirmed cases")
            print("\nWould you like to see the confirmed cases for  random country? yes / no:")
            answer = input()
            if(answer == "yes"):

                print("To select a Random Country, type a number from 0 to 9:")
                list = ["Russia has 17_842_925 confirmed cases",
                "Thailand has 3_628_347 confirmed cases",
                "Poland has 5_957_940 confirmed cases",
                "Iran has 7_159_733 confirmed cases",
                "Mexico has 5_654_311 confirmed cases",
                "Vietnam has  9_472_254 confirmed cases",
                "Japan has 6_504_873 confirmed cases",
                "Spain has 11_508_309 confirmed cases"
                "Netherlands has 7_899_893 confirmed cases"]

                num = input()
                if(num == "0"):
                    print(list[0])
                if(num == "1"):
                    print(list[1])
                if(num == "2"):
                    print(list[2])
                if(num == "3"):
                    print(list[3])
                if(num == "4"):
                    print(list[4])
                if(num == "5"):
                    print(list[5])
                if(num == "6"):
                    print(list[6])
                if(num == "7"):
                    print(list[7])
                if(num == "8"):
                    print(list[8])
                if(num == "9"):
                    print(list[9])
            if(answer == "yes"):
                print("\nWould you like to go back to the home page? yes \ no:")
                answer2 = input()
                if(answer2 == "yes"):
                    continue
                if(answer2 == "no"):
                    print("\nAlright, have a nice day and dont forget to wear a mask at all times!")
                    break

        elif Choice == "2":
            print("\nTo prevent the spread of COVID-19: \nWash your hands regularly, with soap and water and if you are unable to wash your hands, use a 70% alcohol-based hand sanitiser.")
            print("Maintain social distancing of at least 2 meters.")
            print("Avoid touching your face especially your eyes, nose and mouth.")
            print("When coughing or sneezing try to direct the sneeze or cough into your arm and bend your elbow to cover your mouth and nose from spreading germs.")
            print("Stay at home if you are showing symptops or feeling unwell.")
            print("Seek immediate Medical attention if you are having issues breathing/ heaving breathing, fever or coughing.")
            print("Follow your doctors advice and follow the directions given by your local health department/ professional.")
            print("\nWould you like to go back the home page? yes / no:")
            answer4 = input()
            if(answer4 == "yes"):
                continue
            if(answer4 == "no"):
                print("\nAlright, have a nice day and dont forget to wear your mask at all times!")
                break
        elif Choice == "3":
            print("\nMost comman symptoms: \nfever \ndry cough \nfatigue")
            print("\nLess comman symptoms: \nsore throat \nbody and musscle pain \ndiarrhoea \nloss of taste and smell \nheadache ")
            print("\nSerious Symptoms: \ndifficulty breathing \nchest pain or pressure \nloss of speech or movement")
            print("\nWould you like to go back to the home page? yes \ no:")
            answer5 = input()
            if(answer5 == "yes"):
                 continue
            if(answer5 == "no"):
                print("\nAlright, have a nice day and dont forget to waer a mask at all times!")
                break

        elif Choice == "4":
            print("\nIf you experience COVID-19 symptoms, go into self isolation, drink plenty of fluids to stay hydrated, and eat healthy foods. Avoid contact with family memebrs and loved ones who are high risk. Use a seperate bathroom if possible. Desinfect and clean \nfrequently touched surfaces.")
            print("\nWould you like to go back to home page/ yes / no:")
            answer6 = input()
            if(answer6 == "yes"):
                continue
            if(answer6 == "yes"):
                print("\nAlright, have a nice day and wear your mask at all times!")
                break

        elif Choice == "5":
            print("\nDo you have any COVID-19 symptoms? yes \ no:")
            answer7 = input()
            if(answer7 == "yes"):
                print("Is your temperature above 38.5°C? yes / no:")
                answer8 = input()
                if(answer8 == "yes"):
                    print("\nIn which country are you select an option below: \n1.SA\n2.USA\n3.China\nEnter option(1/2/3):")
                    answer9 = input()
                    if(answer9 == "1"):
                        print("The total cases in SA is now:", SA + 1)
                        print("You have COVID-19 please seek treatment at your nearest hospital")
                        
                    elif(answer9 == "2"):
                        print("The total cases in USA is now:", USA + 1)
                        print("You have COVID-19 please seek treatment at your nearest hospital")
                        print("\nWould you like to go back to the home page? yes / no:")

                    elif(answer9 == "3"):
                        print("The total cases in China is now:", China + 1)
                        print("You have COVID-19 please seek treatment at your nearest hospital")
                        print("\nWould you like to go back to the home page? yes / no:")
                        answer10 = input()
                        if(answer10 == "yes"):
                            continue
                        if(answer10 == "no"): 
                            print("\nAlright, have a nice day and keep your mask on at all times!")
                            break
                if(answer8 == "no"):
                    print("You dont have COVID-19")
                    print("\nWould you like to go back to home page? yes \ no:")
                    answer11 =input()
                    if(answer11 == "yes"):
                        continue
                    if(answer11 == "no"):
                        print("\nAlright have a nice day and keep your mask on at all times!")
                        break
            if(answer7 == "no"):
                print("You do not have COVID-19")
                print("\nWould you like to go back to home page? yes / no:")
                answer12 = input()
                if(answer12 == "yes"):
                     continue
                if(answer12 == "no"):
                    print("\nAlright, have a nice day and keep your mask on at all times")
                    break

        elif Choice == "6":
            print("\nAlright, have a nice day and keep your mask on at all time!")
            break
                                                
                                        


                    

