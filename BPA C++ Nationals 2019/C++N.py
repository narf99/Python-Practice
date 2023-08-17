class Course():
    def __init__(self, name:str, rating:float, slope:int):
        self.name = name
        self.rating = rating
        self.slope = slope
    
    def __str__(self) -> str:
        return self.name + " " + str(self.rating) + " " + str(self.slope)

class PlayedCourse():
    def __init__(self, course:Course, score:int, nineHoles:bool):
        self.course = course
        self.score = score
        self.nineHoles = nineHoles
    
    def __str__(self):
        return str(self.course.name) + " " + str(self.score) + " " + str(self.nineHoles)

class Member():
    def __init__(self, name:str, id:int, courseScores:list):
        self.name = name
        self.id = id
        self.courseScores = courseScores
    
    def __str__(self) -> str:
        """ full return
        returnString = self.name + " " + str(self.id) + " "
        for i in self.courseScores:
            returnString += str(i)

        return returnString """
        
        return self.name + " " + str(self.id) + " " + str(self.courseScores[0][0])

def display():
    """This displays all of the menu options and asks the user for what to do"""
    for i in range(len(courses)):

        print(str(i+1) + ". " + courses[i].name)

    print("7. Member List \n8. Exit")

    print("Please pick a course number or exit")

    return getNumFromUser(1, 8)

def sort(data, courseNumber):
    def sortFunc(e):
        """This is a sort function that sorts nested lists based on the second value in the list"""
        return e[1]
    
    print("\n" + data[0].courseScores[courseNumber][0])
    
    strictData = [] # this is sorted [name, course handicap]

    # go through all the data
    for i in range(len(data)):

        # make sure the member has played the course in question
        if len(data[i].courseScores)>courseNumber:
            # add the name of the member and the course handicap to the other data list
            strictData.append([data[i].name, data[i].courseScores[courseNumber][3]]) # this makes it a lot easier to work with
    
    # sort the data
    strictData.sort(key = sortFunc, reverse = True)

    # display the course info
    for i in range(len(strictData)):
        print(str(i+1) + ".\t" + strictData[i][0] + "\tHandicap: " + str(strictData[i][1]))
    
    print("\n")

    strictData = ""

def round(numToRound:float, placesToRoundTo=0) -> (int):
    """ this rounds a given number. doesn't round 5 up and the number of places to round to means the number of decmile places you want"""
    return int(format(numToRound,".{}f".format(placesToRoundTo)))

def getNumFromUser(minNum:int, maxNum:int, num = "", values = None) -> int:
    """Min and max numbers are inclusive. num and values are for recursive function calls"""
    
    # make the list holding the right values this is in a if statment so we dont have to recreate the list ever recursive call
    if values == None:
        values = []
        for i in range(minNum, maxNum+1):
            values.append(str(i))
    
    # get the number from the user and make sure its actually a number
    num = input("Please input a number from " + str(minNum) + " to " + str(maxNum) + " \n: ")
    while num not in values:
        num = input("Please input a number from " + str(minNum) + " to " + str(maxNum) + " \n: ")
    
    # make sure its the right number
    for i in range(minNum, maxNum+1):
        if int(num) == i:
            return i
    
    return getNumFromUser(minNum, maxNum, num, values)

data = []

for i in open("C++ Nationals\Golf Data.txt", "r"):
    data.append(i[:-1])

rawCourses = data[0:18]

rawMemebers = data[18:len(data)]

data = ""

courses = []

for i in range(0, len(rawCourses), 3):
    courses.append(Course(rawCourses[i], float(rawCourses[i+1]), int(rawCourses[i+2])))

rawCourses = ""

members = []

for i in range(0, len(rawMemebers), 14):
    
    membersCourses = []
    
    finalCourses = []
    
    # this takes all the courses the member has played and adds them to a list
    for I in range(12):
        
        membersCourses.append(rawMemebers[i+I+2].split(" "))

        newCourse = []
        
        # this takes all the scores the member has gotten on the specifec course and adds them to a list
        for x in range(1, len(membersCourses[I])-1):
            
            if I % 2 == 0:
                
                newCourse.append(PlayedCourse(courses[int(I/2)], int(membersCourses[I][x]), True))
            
            else:
                
                newCourse.append(PlayedCourse(courses[int(I/2)], int(membersCourses[I][x]), False))

        membersCourses[I] = newCourse
    
    newCourse = ""

    # this finaly moves all the courses to a list with 9 hole and 18 hole games combinded in one list
    for I in range(0, len(membersCourses), 2):
        
        if membersCourses[I] != []:

            # Modified Gross Score
            mgs = 0

            # 18 holes more then 5
            if len(membersCourses[I+1]) > 5:
                
                # more then 20
                if len(membersCourses[I+1]) > 20:
                
                    for x in range(20):
                        mgs += membersCourses[I+1][x].score
                    
                    mgs /= 20
                
                # less then 20
                elif len(membersCourses[I+1]) < 20:

                    for x in range(len(membersCourses[I+1])):
                        mgs += membersCourses[I+1][x].score

                    mgs /= len(membersCourses[I+1])
            
            # nine holes greater then 10
            elif len(membersCourses[I]) > 10:

                # more then 20
                if len(membersCourses[I]) > 20:

                    for x in range(20):
                    
                        mgs += membersCourses[I][x].score
                    mgs /= 20
                
                # less then 20
                elif len(membersCourses[I]) < 20:

                    for x in range(len(membersCourses[I])):
                    
                        mgs += membersCourses[I][x].score
            
                    mgs /= len(membersCourses[I])
            
            # less then 10 nine and 18 holes
            elif len(membersCourses[I]) < 10 and len(membersCourses[I+1]) < 10:
                
                for x in range(len(membersCourses[I])):
                    
                    mgs += membersCourses[I][x].score*2
                
                for x in range(len(membersCourses[I+1])):

                    mgs += membersCourses[I+1][x].score
                
                mgs /= (len(membersCourses[I]) + len(membersCourses[I+1]))

            # handicap index
            mgs = ((mgs - membersCourses[I][0].course.rating) * 113) / membersCourses[I][0].course.slope

            # course handicap
            mgs = (mgs * 0.96 * membersCourses[I][0].course.slope) / 113
            
            mgs = round(mgs, 0)

            finalCourses.append([membersCourses[I][0].course.name, membersCourses[I], membersCourses[I+1], mgs])
    
    mgs = ""
    membersCourses = ""

    members.append(Member(rawMemebers[i], rawMemebers[i+1], finalCourses))

    finalCourses = ""

rawMemebers = ""

whatDo = display()

while whatDo != 8:

    if whatDo == 7: # Member List

        print("#\tName\t\tMembership ID")
        
        for i in range(len(members)):

            print(str(i+1) + "\t" + members[i].name + "\t" + str(members[i].id))
        
        input("Press Enter to Return")
    
    else: # all of the courses
        for i in range(6):
            if whatDo == i+1:
                sort(members, i)
                input("Press Enter to Return")
    
    whatDo = display()