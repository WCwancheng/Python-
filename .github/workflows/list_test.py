
list_t = [1,2,5,4,8,5,415,41,22,4,5,55]

#列表去重,直接循环处理
def removeZList1():
    print(list_t)
    list_1 = []
    for ls in list_t:
        if ls not in list_1:
            list_1.append(ls)
    print(list_1)

def removeZList2():
    print(list_t)
    list_2 = list(set(list_t))
    print(list_2)

def main():
    removeZList1()
    removeZList2()

if __name__=='__main__':
    main()