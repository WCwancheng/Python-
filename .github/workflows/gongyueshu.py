num_a = 0
num_b = 0

#循环遍历
def printGYS1(a,b):
    for i in range(min(a,b),0,-1):
        if a % i ==0 and b % i == 0: 
            print("输入的两个数的最大公约数为 %d " % i)
            break
#辗转相除法 不递归
def printGYS2(a, b):
    while a != 0:
        a, b = b % a, a
    print("输入的两个数的最大公约数为 %d " % b)
    return b
#辗转相除法递归
def printGYS3(a,b):
    if b == 0:
        print("输入的两个数的最大公约数为 %d " % a)
    else:
        printGYS3(b,a%b)

#最相减法
def printGYS4(a,b):
    big = a > b and a or b
    small = a < b and a or b
    if big == small:
        print("输入的两个数的最大公约数为 %d " % small)
    else:
        c = big - small
        printGYS4(c,small)


def main():
    num_a = int(input("输入第一个整数："))
    num_b = int(input("输入第二个整数："))
    printGYS1(num_a,num_b)
    printGYS2(num_a,num_b)
    printGYS3(num_a,num_b)
    printGYS4(num_a,num_b)

if __name__=='__main__':
    main()