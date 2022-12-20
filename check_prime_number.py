import math
def prime(n):

    flag = True

    if n == 0 or n == 1 :
        flag = False
        return flag

    if n <= 3:
        return flag

    if n % 2 == 0:
        flag = False
        return flag

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            flag = False
            return flag
    else:
        return flag

for x in range(20):
    if prime(x):
        print(x,"è primo")
    else:
        print(x,"non è primo")
