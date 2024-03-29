Input = input("Calculator ") 
#Input = "1+(2+2)"
Input = Input.replace(" ","")

def isNumber(strToTest):
    Math = ["+","-","/","*","%","(",")"] 
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
            if Input[Prog] == "(" or Input[Prog] == ")":
                checkNumList.append(True)
                mainList.append(Input[Prog])
            else:
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
        if Operator == listToTest[Prog]:
            return (True, Prog)
    return (False, listLen+1)

def calcSpecialOpe(listToCalc):
    i = 0
    while i < len(listToCalc):
        (hasMin,minPos) = findOpePos(listToCalc,"-")
        if hasMin:
            listToCalc[minPos] = listToCalc[minPos]+listToCalc[minPos+1]
            listToCalc.pop(minPos+1)
        (hasMul,mulPos) = findOpePos(listToCalc,"*")
        if hasMul:
            if listToCalc[mulPos+1] == "*":
                listToCalc[mulPos] = listToCalc[mulPos] + listToCalc[mulPos+1]
                listToCalc.pop(mulPos+1)
        i=i+1
    return listToCalc

mainList = calcSpecialOpe(mainList)

def calculator(listToCalc):
    Number = 0
    Pos = 0

    while len(listToCalc) > 1:
        (hasMul, mulPos) = findOpePos(listToCalc,"*") #Does the listToCalc have a multiplikation symbol and where is it?
        (hasDiv, divPos) = findOpePos(listToCalc,"/") #Does the listToCalc have a divide symbol and where is it?
        (hasMin, minPos) = findOpePos(listToCalc,"-") #Does the listToCalc have a minus symbol and where is it?
        (hasAdd, addPos) = findOpePos(listToCalc,"+") #Does the listToCalc have a addition symbol and where is it?
        (hasExp, expPos) = findOpePos(listToCalc,"**") #Does the listToCalc have a exponential symbol and where is it?
        (hasMod, modPos) = findOpePos(listToCalc,"%") #Does the listToCalc have a modulus symbol and where is it?
        if hasExp:
            Pos = expPos
            Number = float(listToCalc[Pos-1]) ** float(listToCalc[Pos+1])

        elif mulPos < divPos and hasMul:
            Pos = mulPos
            Number = float(listToCalc[Pos-1]) * float(listToCalc[Pos+1])

        elif divPos < mulPos and hasDiv:
            Pos = divPos
            Number = float(listToCalc[Pos-1]) / float(listToCalc[Pos+1])

        elif hasMod:
            Pos = modPos
            Number = float(listToCalc[Pos-1])%float(listToCalc[Pos+1])

        elif minPos < addPos and hasMin:
            Pos = minPos
            Number = float(listToCalc[Pos-1]) - float(listToCalc[Pos+1])

        elif addPos < minPos and hasAdd:
            Pos = addPos
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
            answer =  sliceParen(ListToSlice,0,0)
            return answer
        elif "(" not in ListToSlice and ")" not in ListToSlice:
            calcList = calculator(ListToSlice)
            return calcList
    return answer

Answer = sliceParen(mainList,0,0)

if float(Answer)%1 == 0:
    Answer = int(Answer)
    print(Answer)
else:
    Answer = float(Answer)
    print(Answer)