def fac(n):
	num = 20
	factorial = 1
	factorial_n = num
	if num < 0:
		print("负数没有阶乘")
	elif num == 0:
		print("0的阶乘是1")
	else:
		for i in range(1,num+1):
			factorial = factorial * i
		print("%d的阶乘为%d" % (num,factorial))

		for i in range(1,num):
			factorial_n = factorial_n * i
		print("%d的阶乘为%d" % (num,factorial_n))

		print("递归阶数 %d" % fac_d(num))

#阶乘递归
def fac_d(n):
	if n == 1:
		return 1
	return n * fac_d(n-1)


#斐波那契数列 ，递归
def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    return fib_recur(n-1) + fib_recur(n-2)

#斐波那契数列 for循环
def fib_xk(n):
    count = 0
    ls = [0] * (n + 1)
    for i in range(1,n + 1):
        current = 0
        if i == 1 or i == 2:
            ls[i] = 1
        else:
            current = (ls[i - 1] + ls[i - 2])
            ls[i] = current

    print(ls[n])
    return count

#斐波那契数列 迭代
def fib_died(n):
    i,num1,num2 = 0,1,1
    res = []
    while i < n:
        res.append(num1)
        num1,num2 = num2,num1 + num2
        i = i + 1
    print(res[len(res)-1])

def main():
    fac(20)
    print(fib_recur(15))
    fib_xk(15)
    fib_died(15)

if __name__=='__main__':
    main()