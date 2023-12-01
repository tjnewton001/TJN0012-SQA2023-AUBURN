'''
Taylor Newton
Dec 1, 2023
'''
from pickle import NONE
import random 
import scanner



def fuzzUserName(val1):
   res = scanner.isValidUserName(val1)
   return res  

def fuzzPassword(val):
    res =scanner.isValidPasswordName(val)
    return res

def fuzzKey(val):
    res =scanner.isValidKey(val)
    return res

def fuzzSecret(val):
    res = scanner.checkIfValidSecret(val)
    return res

def fuzzScan(val,val2):
    res = scanner.scanUserName(val,val2)
    return res

def simpleFuzzer(): 
    #Positive Testing for isValidUserName
    a = 'TestName'
    result = fuzzUserName(a)
    #negative testing
    print("-"*10)
    print("Fuzz scanner.isValidUserName testing, should be True False False")
    print(result)
    b = "email"
    result = fuzzUserName(b)
    print(result)
    c = NONE
    result = fuzzUserName(c)
    print(result)

    #Positive Testing for isValidKey
    a = 'password'
    result = fuzzKey(a)
    #negative testing
    print("-"*10)
    print("Fuzz scanner.isValidKey testing, should be True False False")
    print(result)
    b = "badKey"
    result = fuzzKey(b)
    print(result)
    c = NONE
    result = fuzzKey(c)
    print(result)
    
    #Positive Testing for isValidPasswordName
    a = 'key'
    result = fuzzPassword(a)
    #negative testing
    print("-"*10)
    print("Fuzz scanner.isValidPasswordName testing, should be True False False")
    print(result)
    b = "_file"
    result = fuzzPassword(b)
    print(result)
    c = NONE
    result = fuzzPassword(c)
    print(result)

    #Positive Testing for checkIfValidSecret
    a = 'secret'
    result = fuzzSecret(a)
    #negative testing
    print("-"*10)
    print("Fuzz scanner.checkIfValidSecret testing, should be True False False")
    print(result)
    b = "[]"
    result = fuzzSecret(b)
    print(result)
    c = NONE
    result = fuzzSecret(c)
    print(result)

    #Positive Testing for scanUserName
    a = 'user'
    aa = ['secret']
    result = fuzzScan(a,aa)
    #negative testing
    print("-"*10)
    print("Fuzz scanner.scanUserName testing, should be ['secret'] [] []")
    print(result)
    b = "username"
    bb = ["[]"]
    result = fuzzScan(b,bb)
    print(result)
    c = NONE
    cc = NONE
    result = fuzzScan(c,cc)
    print(result)
    pass 

if __name__=='__main__':
    simpleFuzzer()




