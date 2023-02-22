Input = input("Lommeregner ")
Input.replace(" ","")

def isNumber(strToTest, specific):
    Math = ["+","-","/","*"]
    mathNum = 0
    for mathNum in range(4):
        if Math[mathNum] in strToTest:
            if specific:
                return mathNum
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
    mainList = [""]
    boolList = []
    numList = []
    for Prog in range(strLen):
        if isNumber(Input[Prog],False):
            numList.append((Input[Prog]))
        elif not isNumber(Input[Prog],False):
            if len(numList) > 0:
                mainList.append(listAdd(numList))
                numList.clear()
                boolList.append(True)
            boolList.append(False)
            mainList.append(Input[Prog])
    if len(numList) > 0:
        mainList.append(listAdd(numList))
        numList.clear()
        boolList.append(True)
    mainList.remove("")
    
    return mainList

print(findToken(Input))

"""
def funcVar1(Input):
    if "+" in Input:
        List = Input.split("+")
        Var1 = List[0]
    elif "-" in Input:
        List = Input.split("-")
        Var1 = List[0]
    elif "*" in Input:
        List = Input.split("*")
        Var1 = List[0]
    elif "/" in Input:
        List = Input.split("/")
        Var1 = List[0]
    return float(Var1)

def funcVar2(Input):
    if "+" in Input:
        List = Input.split("+")
        Var2 = List[1]
    elif "-" in Input:
        List = Input.split("-")
        Var2 = List[1]
    elif "*" in Input:
        List = Input.split("*")
        Var2 = List[1]
    elif "/" in Input:
        List = Input.split("/")
        Var2 = List[1]
    return float(Var2)

if "+" in Input:
    print(funcVar1(Input)+funcVar2(Input))
elif "-" in Input:
    print(funcVar1(Input)-funcVar2(Input))
elif "*" in Input:
    print(funcVar1(Input)*funcVar2(Input))
elif "/" in Input:
    print(funcVar1(Input)/funcVar2(Input))
"""