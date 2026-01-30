while True:
    print("\n Welcome to grading system")
    print("select an option")
    print("1.Check your grade")
    print("2.exit")

    option=(input("Enter option:"))
    if option =="1":
        marks =int(input("Enter marks:"))
        if marks >=1 and marks <=10:
         print("E")
         if marks >=11 and marks <=15:
            print("D-")
         if marks >=16 and marks <=20:
            print("D")
        if marks >=21 and marks <=25:
         print("D+")
        if marks >=26 and marks <=30:
         print("C-")
        if marks >=31 and marks <=35:
            print("C")
        if marks >=36 and marks <=40:
            print("C+")
        if marks >=41 and marks <=45:
         print("B-")
         if marks >=46 and marks <=50:
            print("B")
        if marks >=51 and marks <55:
            print("B+")
        if marks >=56 and marks <=60:
            print("A")
        if marks >=61 and marks <=100:
            print("B+")
        else:
           print("invalid marks")
    elif option=="2":
        print("\nThankyou for using the system.Come again")
        break
    else :
       print("\nInvalid input,please try again.")