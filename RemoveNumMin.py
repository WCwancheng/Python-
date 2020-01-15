#删除K个数字后的最小值
#给出一个整数，从该整数中去掉K个数字，要求剩下的数字形成的新整数尽可能小。
#例子：
#1.输入1593212 去掉3个是数字 返回1212
#2.输入30200 去掉1个数字 返回200
#3.输入10 去掉2个数字 返回0

def RemoveKDigits(num,k):
    num_s = str(num)
    num_length = len(num_s) - k
    stack_ls = []
    top = 0
    for i in range(len(num_s)):
        n = num_s[i]
        top = i
        while top > 0 and stack_ls != [] and stack_ls[-1] > n and k > 0:
            stack_ls.pop()
            top -= 1
            k -= 1
        stack_ls.append(n)
    offest = 0
    while offest < num_length and stack_ls[offest] == '0':
        offest += 1
    return offest == num_length and '0' or int(''.join(stack_ls))

def main():
    reuslt = RemoveKDigits(541270936,3)
    print(reuslt)
    reuslt = RemoveKDigits(30200,1)
    print(reuslt)
    reuslt = RemoveKDigits(10,2)
    print(reuslt)

if __name__=='__main__':
    main()