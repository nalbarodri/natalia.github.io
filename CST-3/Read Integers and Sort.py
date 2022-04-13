# January 14, 2022
#Natalia Alba Rodriguez
# Python program to read integers from a file and sort them

pizzafriday = list()

filename = 'numbers.txt'

with open (filename) as fin:
    for line in fin:
        pizzafriday.append(int(line))


pizzafriday.sort()
print(pizzafriday)

total = sum(pizzafriday)
print (total)

if total > 1:
    for i in range(2, total):
        if (total % i) ==0:
            print(total, "this is not prime")
            break
    else:
        print(total, "yay, this is a prime number")
else:
    print(total, "is not a prime number")
