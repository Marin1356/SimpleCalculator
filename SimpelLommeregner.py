Input = input("Lommeregner ")
Input.replace(" ","")

def isNumber(strToTest):
    Math = ["+","-","/","*"] 
    mathNum = 0
    for mathNum in range(4):
        if Math[mathNum] in strToTest:
            return False
    return True

def listAdd(List):
    Output = ""
    listLen = len(List)
    for Prog in range(listLen):
        Output = Output + List[Prog]
    return Output

def findToken(Input):
    strLen = len(Input)
    Prog = 0
    mainList = []
    checkNumList = [] 
    numList = []
    for Prog in range(strLen):
        if isNumber(Input[Prog]):
            numList.append((Input[Prog]))
        elif not isNumber(Input[Prog]):
            if len(numList) > 0:
                mainList.append(listAdd(numList))
                numList.clear()
                checkNumList.append(True)
            checkNumList.append(False)
            mainList.append(Input[Prog])
    if len(numList) > 0:
        mainList.append(listAdd(numList))
        numList.clear()
        checkNumList.append(True)
    return (mainList, checkNumList)

(mainList, checkNumList) = findToken(Input)
print(findToken(Input))

def findOpePos(listToTest, Operator): 
    listLen = len(listToTest)
    Prog = 0
    for Prog in range(listLen):
        if not isNumber(listToTest[Prog]):
            if Operator == listToTest[Prog]:
                return (True, Prog)

def calculator(listToCalc):
    length = len(listToCalc)
    checkedOperators = 0
    if findOpePos(listToCalc,"*"[0]):
        Pos = findOpePos(listToCalc,"*")[1]
        Number = float(listToCalc[Pos-1]) * float(listToCalc[Pos+1])
        return Number

    elif findOpePos(listToCalc,"/"[0]):
        Pos = findOpePos(listToCalc,"/")[1]
        Number = float(listToCalc[Pos-1]) / float(listToCalc[Pos+1])
        return Number

    elif findOpePos(listToCalc,"-"[0]):
        Pos = findOpePos(listToCalc,"-")[1]
        Number = float(listToCalc[Pos-1]) - float(listToCalc[Pos+1])
        return Number

    elif findOpePos(listToCalc,"+"[0]):
        Pos = findOpePos(listToCalc,"+")[1]
        Number = float(listToCalc[Pos-1]) + float(listToCalc[Pos+1])
        return Number

