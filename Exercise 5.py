def getdate():
    import datetime
    return datetime.datetime.now()

# Excersise - 1 // Diat - 2
def take(k):
    if k==1:
        mode=int(input("Please enter you choice\n"
                       "1 : To view\n"
                       "2 : To Add\n"))
        if mode==1:
            name=int(input("Please enter 1 for Ram, 2 for Shyam and 3 for Geeta\n"))
            if name==1:
                with open("RamExcersise.txt") as Ram:
                    for i in Ram:
                        print(i, end="")
            elif name==2:
                with open("ShyamExcersise.txt") as Shyam:
                    for i in Shyam:
                        print(i, end="")
            elif name==3:
                with open("GeetaExcersise.txt") as Geeta:
                    for i in Geeta:
                        print(i, end="")
            else:
                print("Please enter valid input : 1 for Ram, 2 for Shyam and 3 for Geeta\n")
        elif mode==2:
            name=int(input("Please enter 1 for Ram, 2 for Shyam and 3 for Geeta\n"))
            if name==1:
                value=input("Type here\n")
                with open("RamExcersise.txt", "a") as Ram:
                    Ram.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
            elif name==2:
                value=input("Type here\n")
                with open("ShyamExcersise.txt", "a") as Shyam:
                    Shyam.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
            elif name==3:
                value=input("Type here\n")
                with open("GeetaExcersise.txt", "a") as Geeta:
                    Geeta.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
            else:
                print("Please enter valid input : 1 for Ram, 2 for Shyam and 3 for Geeta\n")
        else:
            print("Please enter valid input : \n"
                  "1 : To View \n"
                  "2 : To Add\n")
    elif k==2:
        mode = int(input("Please enter you choice\n"
                         "1 : To view \n"
                         "2 : To Add\n"))
        if mode==1:
            name=int(input("Please enter 1 for Ram, 2 for Shyam and 3 for Geeta\n"))
            if name==1:
                with open("RamDiat.txt") as Ram:
                    for i in Ram:
                        print(i, end="")
            elif name==2:
                with open("ShyamDiat.txt") as Shyam:
                    for i in Shyam:
                        print(i, end="")
            elif name==3:
                with open("GeetaDiat.txt") as Geeta:
                    for i in Geeta:
                        print(i, end="")
            else:
                print("Please enter valid input : 1 for Ram, 2 for Shyam and 3 for Geeta\n")
        elif mode==2:
            name=int(input("Please enter 1 for Ram, 2 for Shyam and 3 for Geeta\n"))
            if name==1:
                value=input("Type here\n")
                with open("RamDiat.txt", "a") as Ram:
                    Ram.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
            elif name==2:
                value=input("Type here\n")
                with open("ShyamDiat.txt", "a") as Shyam:
                    Shyam.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
            elif name==3:
                value=input("Type here\n")
                with open("GeetaDiat.txt", "a") as Geeta:
                    Geeta.write(str([str(getdate())]) + ": " + value + "\n")
                print("Successfully Written")
            else:
                print("Please enter valid input : 1 for Ram, 2 for Shyam and 3 for Geeta\n")
        else:
            print("Please enter valid input : \n"
                  "1 : To View \n"
                  "2 : To Add\n")
    else:
        print("Please enter valid Input, Press 1 for Excersise and 2 for Food")


selection=int(input("Please enter 1 for Excersise and 2 for Food\n"))

print(take(selection))