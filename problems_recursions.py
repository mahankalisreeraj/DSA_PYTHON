'''
Factorial of a number
'''
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(3))


'''
Nth Fibonacci number
'''
def fibonacci_Series(n):
    if n <= 1:
        return n
    return fibonacci_Series(n-1) + fibonacci_Series(n-2)
print(fibonacci_Series(2))
    
'''
Sum of N natural numbers
'''

def sum1(n):
    if n == 1:
        return 1
    return  n + sum1(n-1)

print(sum1(2))

'''
Print numbers form 1 to N and N to 1
'''

def print_1_n(n):
    if n == 0:
        return 
    print_1_n(n-1)
    print(n,end = " ")

def print_n_1(n):
    if n == 0:
        return 
    print(n,end = " ")
    print_n_1(n-1)

print_1_n(5)
print()
print_n_1(5)

'''
reversing the string recursively
'''

def reverse(s,ans,n):
    if n == -1:
        return ans
    return reverse(s,ans+s[n],n-1)
    
    
s = "hello"
print(reverse(s,"",len(s)-1))

'''
power of a number
'''
# x ^ n
def power(x,n):
    if n == 0:
        return 1
    return x * power(x,n-1)

print(power(7,2))

'''
Check if a string is palindrome
''' 
def is_palindrome(s,l,r):
    if l >= r:
        return True 
    if s[l] != s[r]:
        return False
    return is_palindrome(s,l+1,r-1)
    
s = 'ababa'
print(is_palindrome(s,0,len(s)-1))

'''
counting number of subarray of a given sum
'''
def subarray_sum(arr,i,j,n,target,cnt):
    if i == n:
        return cnt
    if j > n:
        return subarray_sum(arr, i + 1, i + 1, n, target, cnt)
    if sum(arr[i:j]) == target:
        cnt += 1
    return subarray_sum(arr, i, j + 1, n, target, cnt) 

arr = [1,2,3]
target = 2
print(subarray_sum(arr,0,0,len(arr),target,0))
