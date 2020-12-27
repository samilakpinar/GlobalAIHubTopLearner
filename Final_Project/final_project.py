
#registered students in the system
student = [
    {
    "name":"Şamil",
    "surname":"Akpınar",
    
    }
    ]



temp = False

def takeLesson():

    print("Please enter your five lessons name")
    global lessons
    lessons = list()
    for i in range(5):
        lesson = input("{}. lesson name: ".format(i+1))
        lessons.append(lesson)
    writeLesson()
    grade()


def writeLesson():

    print("\nYou can take a min of 3 and a max of 5 lessons\n")
    global temp
    global myLessons
    

    takeLessonsNumber = int(input("How many lessons do you want to take: "))
    myLessons = []
    if 3 <= takeLessonsNumber <=5:
        z = 0
        while z < 1:
            
            myLessons = list()

            for i in range(takeLessonsNumber):
                takeLesson = input("\nwhich course do you want to take?: ")
                if takeLesson in lessons:
                    myLessons.append(takeLesson)
                else:
                    print("\nLesson not found. Please try again!")
                    z = -1
                    break

            z+=1
    else:
        print("You stayed in class")
        temp = True
        return temp
        
    

    print("\nYour courses registered in the system")

    for i in myLessons:
        print(i)


def grade():

    if temp == False:
        oneLesson = input("\nPlease choose a lesson: ")
        if oneLesson in myLessons:
            midterm = int(input("Please enter your midterm exam result: "))
            final = int(input("Please enter your final exam result: "))
            project = int(input("Please enter your project note result: "))

            examNotes = {"midterm":midterm,"final":final,"project":project}

            grade = (examNotes["midterm"]*(3/10)) + (examNotes["final"]*(1/2)) + (examNotes["project"]*(1/5))


            
            if grade >= 90:
                print("Your grade: AA")

            elif 70 <= grade < 90:
                print("Your grade: BB")

            elif 50 <= grade < 70:
                print("Your grade: CC")
                
            elif 30 <= grade < 50:
                print("Your grade: BB")

            elif grade < 30:
                print("Your grade: FF and you failed")

         
        else:
            print("The lesson attended is not registered")




k = 0
control = False
while k < 3:
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")

    
    for i in student:
        if i["name"] == name.strip(' ') and i["surname"] == surname.strip(' '):
            print("\nWelcome\n")
            control = True
            takeLesson()
            break
        else:
            if k == 2:
                print("\nPlease try again later!\n")
                break
            print("\nThe user is not in the system. Please try again now!\n")

    if control == True:
        break
    k+=1


