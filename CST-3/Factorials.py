#let's write a  program to compute the factorial of a number
#Week 1 - Natalia Alba Rodriguez- CST-111 - January 7th 2022

usernum= int(input("Please enter a number to compute factorial:"))

def factorial(usernum):
    if usernum == 0:
        return 1
    else:
        return usernum * factorial(usernum-1)
print(factorial(usernum))

