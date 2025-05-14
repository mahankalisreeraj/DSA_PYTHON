# recursively printing 1 2 3 4 5 4 3 2 1

def res1(n,peak):
    if n == peak:
        return res2(n)
    print(n+1,end =" ")
    return res1(n+1,peak)

def res2(n):
    if n == 1:
        return 
    print(n-1,end = " ")
    return res2(n-1)

n = int(input("Enter starting number:"))
peak = int(input("Enter breaking point:"))
res1(n-1,peak)

#Using only one function
def funcn(n,m=0):
    if n == m:
        return 
    print(m+1,end = " ")
    funcn(n,m+1)
    if m+1 != 5:
        print(m+1,end = " ")
        
funcn(5)

#recurvisely Printing 5 4 3 2 1 2 3 4 5
def funcn(n):
    if n == 0:
        return 
    print(n,end = " ")
    funcn(n-1)
    if n != 1:
        print(n,end = " ")

funcn(5)

#above + printing only even numbers
def funcn(n):
    if n == 0:
        return 
    if n % 2 == 0:
        print(n,end = " ")
    funcn(n-1)
    if n % 2 == 0:
        print(n,end = " ")

#factorial 
def funcn(n):
    if n == 1:
        return 1
    return n*funcn(n-1)

print(funcn(5))


#Prime Number
def is_prime(n,i = 2):
    if i*i > n:
        return True 
    if n % i == 0:
        return False 
    return is_prime(n,i+1)

print(is_prime(7))

#reverse number
def rev_num(n,re = 0):
    if n == 0:
        return re 
    else:
        d = n % 10
        re = (re*10)+d 
        return rev_num(n//10,re)

print(rev_num(int(input("Enter number:"))))


# min steps to reach 0 of a number 

def funcn(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + funcn(n//2)
    else:
        return 1 + min(funcn(n-1),funcn(n+1))
        
print(funcn(15))


#Sum of elements using recursion
def funcn(l,i=0):
    if i == len(l):
        return 0
    return l[i] + funcn(l,i+1)

l = [1,2,3,4,5]
print(funcn(l))

#count of prime numbers in a list using recursion

def is_prime(n,i = 2):
    if i*i > n:
        return True 
    if n % i == 0:
        return False 
    return is_prime(n,i+1)

def funcn(l,i=0):
    if i == len(l):
        return 0
    if is_prime(l[i]):
        return 1 + funcn(l,i+1)
    else:
        return funcn(l,i+1)

l = [1,2,3,4,5]
print(funcn(l,0))


#fibonacci series
def funcn(n):
    if n == 0 or n == 1:
        return n 
    return funcn(n-1) + funcn(n-2) 

print(funcn(5))