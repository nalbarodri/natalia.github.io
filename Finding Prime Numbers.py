#Find prime numbers within a range (1-100)

begin = 1
stop = 10000

for i in range (begin, stop):
    if i >1:
        for j in range(2,i):
            if (i % j==0):
                break
        else:
            print(i)
