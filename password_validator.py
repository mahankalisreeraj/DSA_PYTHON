'''
You are given a Str. Your task is to find the number of checks that is not satisfied by the string str by checking the validation or the string str if it's a strong password or not. A password is a strong password only it:
It contains at least 6 characters and at most 22 characters.
It must contain at least one uppercase character.
It must contain at least one lowercase character.
It must contain at least two special characters (@, !, &,^,%,#)
It must contain at least one numeric value.
It must not contain any same consecutive character.
'''
str1 = input("Enter Password : ")
islen,isnum,splchar,lower,upper,isconsecqutive = len(str1),False,0,False,False,True
for i in range(islen):
    if str1[i].isupper():
        upper = True 
    if str1[i].islower():
        lower = True 
    if str1[i].isdigit():
        isnum = True 
    if str1[i] in ['@','!','&','%','#']:
        splchar += 1
    if i != 0 and str1[i-1] == str1[i]:
        isconsecqutive = False

if islen >= 6 and islen <= 22:
    if isconsecqutive:
        if isnum and lower and upper and splchar >= 2:
            print("Your Password is Strong!!!!!")
        else:
            print("Password must contain atleast one uppercase,one lowercase,one digit & atleast 2 special characters") 
    else:
        print("No two letters should be consecutive")
else:
    print("Password isn't the specified length")
    
