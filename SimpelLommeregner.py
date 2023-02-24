Input = input("Calculator ") 
Input = Input.replace(" ","")

def isNumber(strToTest):
    Math = ["+","-","/","*","(",")"] 
    mathNum = 0
    for mathNum in range(6):
        if Math[mathNum] is strToTest:
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

def findOpePos(listToTest, Operator): 
    listLen = len(listToTest)
    Prog = 0
    for Prog in range(listLen):
        if not checkNumList[Prog]:
            if Operator == listToTest[Prog]:
                return (True, Prog)

def calculator(listToCalc):
    Number = 0
    Pos = 0

    while listToCalc >1:
        if findOpePos(listToCalc,"*"[0]):
            Pos = findOpePos(listToCalc,"*")[1]
            Number = float(listToCalc[Pos-1]) * float(listToCalc[Pos+1])

        elif findOpePos(listToCalc,"/"[0]):
            Pos = findOpePos(listToCalc,"/")[1]
            Number = float(listToCalc[Pos-1]) / float(listToCalc[Pos+1])

        elif findOpePos(listToCalc,"-"[0]):
            Pos = findOpePos(listToCalc,"-")[1]
            Number = float(listToCalc[Pos-1]) - float(listToCalc[Pos+1])

        elif findOpePos(listToCalc,"+"[0]):
            Pos = findOpePos(listToCalc,"+")[1]
            Number = float(listToCalc[Pos-1]) + float(listToCalc[Pos+1])
        
        listToCalc[Pos] = Number
        listToCalc.pop(Pos-1)
        listToCalc.pop(Pos)
    return listToCalc[0]

def sliceParen(ListToSlice,startPos,lastStartParen):
    Prog = startPos
    calcList = []
    for Prog in range(startPos,len(ListToSlice)):
        if "(" == ListToSlice[Prog]:
            lastStartParen = Prog
            answer =  sliceParen(ListToSlice,Prog+1,lastStartParen)
            return answer
        if ")" == ListToSlice[Prog]:
            calcList = calculator(ListToSlice[lastStartParen+1:Prog])
            ListToSlice = ListToSlice[:lastStartParen] + [calcList] + ListToSlice[Prog+1:]
            print(ListToSlice)
            answer =  sliceParen(ListToSlice,0,0)
            return answer
        elif "(" not in ListToSlice and ")" not in ListToSlice:
            calcList = calculator(ListToSlice)
            return calcList
    return answer

if any(i.isalpha() for i in mainList):
    print("Error")
else:
    Answer = sliceParen(mainList,0,0)

if float(Answer)%1 == 0:
    Answer = int(Answer)
    print(Answer)
else:
    Answer = float(Answer)
    print(Answer)