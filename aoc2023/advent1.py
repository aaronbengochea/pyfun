import json



def main():
    filePath = "C:\\cygwin64\\home\\cicyf\\aaron\\pyfun\\aoc2023\\advent1.txt"
    possible = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open(filePath, "r") as file:
        content = file.read()

    total = 0
    test = 0
    for item in content.splitlines():
        i = 0
        j = len(item) - 1
        itemNumber = 0
        leftInt = ""
        rightInt = ""
        finalNumber = ""
        iFlag = True
        jFlag = True


        while i < len(item) and iFlag:

            if iFlag:
                for index, number in enumerate(possible):
                    if number in leftInt:
                        intToString = str(index + 1)
                        leftInt = ""
                        leftInt = intToString
                        iFlag = False
                    

            if item[i].isdigit() and iFlag:
                leftInt = ""
                leftInt = item[i]
                iFlag = False

            if iFlag:
                leftInt += item[i]
                i += 1


        while j >= 0 and jFlag:

            if jFlag:
                for index, number in enumerate(possible):
                    if number in rightInt:
                        intToString = str(index + 1)
                        rightInt = ""
                        rightInt = intToString
                        jFlag = False
                        
            if item[j].isdigit() and jFlag:
                rightInt = ""
                rightInt = item[j]
                jFlag = False

            if jFlag:
                rightInt = item[j] + rightInt
                j -= 1
            

        finalNumber = leftInt + rightInt
        #print(leftInt, "--", rightInt)
        itemNumber = int(finalNumber)
        total += itemNumber

    print(total)






if __name__ == "__main__":
    main()