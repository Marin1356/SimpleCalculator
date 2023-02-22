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

def findToken(Input):
    pass

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
print(isNumber("9"))