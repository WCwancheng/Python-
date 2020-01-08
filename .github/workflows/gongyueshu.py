num_a = 0
num_b = 0

def printGYS1(a,b):
    for i in range(min(a,b),0,-1):
        if a % i ==0 and b % i == 0: 
            print("输入的两个数的最大公约数为 %d " % i)
            break

def printGYS2(a, b):
    while a != 0:
        a, b = b % a, a
    print("输入的两个数的最大公约数为 %d " % b)
    return b

def printGYS3(a,b):
    if b == 0:
        print("输入的两个数的最大公约数为 %d " % a)
    else:
        printGYS3(b,a%b)

def main():
    num_a = int(input("输入第一个整数："))
    num_b = int(input("输入第二个整数："))
    printGYS1(num_a,num_b)
    printGYS2(num_a,num_b)
    printGYS3(num_a,num_b)

if __name__=='__main__':
    main()