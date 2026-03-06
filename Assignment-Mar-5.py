# 1. Print Numbers from 1 to n

def num_to_n(n):
    for i in range(1,n+1):
        print(i,end=" ")

n=int(input("Enter n value:"))
num_to_n(n)

# output:
# Enter n value:6
# 1 2 3 4 5 6 


# 2. Print Numbers from m to n

def m_to_n(m,n):
    for i in range(m,n+1):
        print(i,end=" ")

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
m_to_n(m,n)

# output:
# Enter m value:4
# Enter n value:23
# 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23


# 3. Print Numbers from n to 1 in Reverse

def rev_nums(n):
    for i in range(n,0,-1):
        print(i,end=" ")

n=int(input("Enter n value:"))
rev_nums(n)

# output:
# Enter n value:5
# 5 4 3 2 1 


# 4. Print Numbers from n to m in Reverse

def rev_n_to_m(n,m):
    for i in range(n,m-1,-1):
        print(i,end=" ")

n=int(input("Enter n value:"))
m=int(input("Enter m value:"))

rev_n_to_m(n,m)

# output:
# Enter n value:7
# Enter m value:2
# 7 6 5 4 3 2

# 5. Sum of n Natural Numbers

def sum_nums(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return f"Sum of natural numbers from 1 to {n} is {sum}"

n=int(input("Enter n value:"))
print(sum_nums(n))

# output:
# Enter n value:7
# Sum of natural numbers from 1 to 7 is 28

# 6. Factorial of a Number

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return f"Factorial of {n} is {fact}"

n=int(input("Enter n value:"))
print(fact(n))

# output:
# Enter n value:5
# Factorial of 5 is 120

# 7. Sum of m to n Numbers

def sum_nm(m,n):
    sum=0

    for i in range(m,n+1):
        sum+=i
    return f"Sum of natural numbers from {m} to {n} is {sum}"

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

print(sum_nm(m,n))

# output:
# Enter m value:2
# Enter n value:7
# Sum of natural numbers from 2 to 7 is 27

# 8. Product of m to n Numbers

def prod(m,n):
    prod=1

    for i in range(m,n+1):
        prod*=i
    return f"Product of natural numbers from {m} to {n} is {prod}"

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

print(prod(m,n))

# output:
# Enter m value:3
# Enter n value:7
# Product of natural numbers from 3 to 7 is 2520

# 9. Print Factors of a Number

def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")

n=int(input("Enter n value:"))
factor(n)

# output:
# Enter n value:6
# 1 2 3 6 

# 10. Count of Factors

def fact_count(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count

n=int(input("Enter n value:"))
print(fact_count(n))

# output:
# Enter n value:6
# 4

# 11. Prime Number Check

def prime_check(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("Enter n value:"))
print(prime_check(n))

# output:
# Enter n value:45
# False

# 12. Even Numbers from m to n

def even(m,n):
    for i in range(m,n+1):
        if i%2==0:
            print(i,end=" ")

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
even(m,n)

# output:
# Enter m value:2
# Enter n value:22
# 2 4 6 8 10 12 14 16 18 20 22 


# 13.  Odd Numbers from m to n

def odd(m,n):
    
    for i in range(m,n+1):
        if i%2!=0:
            print(i,end=" ")

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

odd(m,n)

# output:
# Enter m value:2
# Enter n value:8
# 3 5 7

# 14. Count of Even and Odd Numbers

def even_odd_count(m,n):
    even=0
    odd=0
    for i in range(m,n+1):
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("Even:",even)
    print("Odd:",odd)

m=int(input("Enter m value:"))
n=int(input("Enter n value:"))

even_odd_count(m,n)

# output:
# Enter m value:2
# Enter n value:88
# Even: 44
# Odd: 43

# 15. Reverse a String

def rev_str(str):
    print("Reverse of String is",str[::-1])

str=input("Enter string:")
rev_str(str)

# output:
# Enter string:Manjunadh
# Reverse of String is hdanujnaM
