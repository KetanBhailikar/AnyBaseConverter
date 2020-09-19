# Getting the inputs and deciding what function
def main():
    global n
    n = ''
    b = int(input("Enter the Base from which you want to Convert:"))
    b1 = int(input("Enter the Base to which you want to Convert:"))
    if (b > 10):
        ToDecimal2(0, b, b1)
    else:
        n = int(input("Enter the Base "+str(b)+" Number :"))
        ToDecimal(n, b, b1)
    print(str(n)+' in Base '+str(b1)+' is : '+finalNum)


# Converting Base 10 to Any other Base:
def ToBaseN(n, b):
    global finalNum
    finalNum = " "
    if n > 1:
        ToBaseN(n//b, b)
    if (len(str((n % int(b))))) == 1:
        finalNum = finalNum + str(str(n % int(b)))
    else:
        finalNum = finalNum + " "+str(str(n % int(b)))+" "


# Converting any number which has a base greater than 10:
def ToDecimal(num, b, b1):
    decimal_value = 0
    base = 1
    iferrornum = num
    while (num):
        last_digit = num % 10
        if(last_digit >= b):
            err(iferrornum, b)
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * b
    ToBaseN(decimal_value, b1)


# Converting any number which has a base greater than 10:
def ToDecimal2(a, b, c):
    global n
    numOfDigs = int(input('Enter the number of digits:'))
    print('Enter the number from left to right!')
    temp = numOfDigs
    deci_val = 0
    while temp != 0:
        x = int(input('Enter digit '+str(numOfDigs-temp+1)+' :'))
        if(x >= b):
            print("Error : The number "+str(x) +
                  " does not exist in Base "+str(b)+"!")
            exit()
        n = n + str(x)
        deci_val = deci_val + (x*(b**(temp-1)))
        temp = temp-1
    ToBaseN(int(deci_val), c)


# Handling Errors
def err(n, b):
    print("Error : "+str(n)+" is not a Base "+str(b)+" Number!")
    exit()


main()
