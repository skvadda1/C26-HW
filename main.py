def totalSetBits(n):
    count = 1
    while(n):
        if(n&1==1):
            break
        count += 1
        n >>= 1
    return count
n = int(input("Enter your number:\n"))
print("Position of first set bit:\n", totalSetBits(n))