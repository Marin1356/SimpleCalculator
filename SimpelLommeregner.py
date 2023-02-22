#Input = input("Lommeregner ")
#Input.replace(" ","")

# findToken("-10+4*4") -> ("-", "10+4*4")
# findToken("+10+4*4") -> ("+", "10+4*4")
# findToken("4") -> ("4", "")
# findToken("10+4*4") -> ("10", "+4*4")
# findToken("") -> ("", False)

def isNumber(strToTest):
    Math = ["+","-","*","/"]
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
    mainList = [""]
    numList = []
    for Prog in range(strLen):
        if isNumber(Input[Prog]):
            numList.append((Input[Prog]))
        elif not isNumber(Input[Prog]):
            if len(numList) > 0:
                mainList.append(listAdd(numList))
                numList.clear()
            mainList.append(Input[Prog])
    if len(numList) > 0:
        mainList.append(listAdd(numList))
        numList.clear()
    mainList.remove("")
    return mainList

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
"""
if findToken("-10+4*4") == ("-", "10+4*4") and findToken("+10+4*4") == ("+", "10+4*4") and findToken("4") == ("4", "") and findToken("10+4*4") == ("10", "+4*4") and findToken("") == ("", False):
    print("det virkede!")
else:
    print("det virkede ikke")
"""

print(findToken("22+12"))