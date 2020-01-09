import string,random

def CreateOneCode():
    model = string.ascii_letters + string.digits
    ls = []
    for i in range(4):
        test = random.sample(model,4)
        test_str = ''.join(test)
        ls.append(test_str)

    test_str2 = '-'.join(ls)
    return test_str2

def main():
    dic = []
    for i in range(1000): 
        dic.append(CreateOneCode())

    dic = set(dic) #去重
    file = open("激活码.txt","w")
    file.write(str(dic)) #保存本地
    file.close()
main()