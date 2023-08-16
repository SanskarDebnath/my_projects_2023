# password checker in most efficient format

import string as s
def charCheck(Val1):
    upperCase = any(c in s.ascii_uppercase for c in Val1)
    lowerCase = any(c in s.ascii_lowercase for c in Val1)
    numeric = any(c in s.digits for c in Val1)
    specialChar = any(c in s.punctuation for c in Val1)
    char_Type = (upperCase + lowerCase + numeric + specialChar)/4.0
    return char_Type

def charLen(Val2):
    strLen = min(1.0,len(Val2)/12.0)
    return strLen

def passCheck(Val3):
    myResult = (charCheck(Val3) + charLen(Val3))/2.0
    if myResult <= 0.625:
        print("Poor password")
    elif myResult <= 0.75 and myResult > 0.625 :
        print("average password")
    elif myResult <= 0.875 and myResult > 0.75:
        print ("good password")
    else:
        print("great password")
    


try:
    password = input("enter password: ")
    if len(password) < 12:
        print("password too short!")
    elif len(password) > 15:
        print("password too long!")
    else:
        passCheck(password)
except:
    print("invalid value entered!")