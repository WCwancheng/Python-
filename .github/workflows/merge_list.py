ls_a = [1,25,2,2,22,0,45,122,512]
ls_b = [1,5,212,4,511]


def Merge1(ls_1,count_1,ls_2,count_2):
    ls_1[count_1:count_1+count_2] = ls_2
    ls_1.sort()
    print(ls_1)

#先对比那个列表的数值最大
def Select_M(ls_1,count_1,ls_2,count_2):
    if ls_1[count_1-1] >= ls_2[count_2-1]:
        Merge2(ls_1,count_1,ls_2,count_2)
    else:
        Merge2(ls_2,count_2,ls_1,count_1)

#遍历列表2，依次插入列表1
def Merge2(ls_1,count_1,ls_2,count_2):
    count = 0
    index = 0
    while count < count_2:
        if ls_1[index] >= ls_2[count]:
            ls_1[index+1:count_1+count+1] = ls_1[index:count_1+count]
            ls_1[index] = ls_2[count]
            count += 1
        if index > count_1+count -1 :
            ls_1[index] = ls_2[count]
            count += 1
        index += 1
    print(ls_1)

def Merge3(ls_1,count_1,ls_2,count_2):
    ls_1[count_1:count_1+count_2] = ls_2 #需要先开辟空间
    while(count_1 >0 and count_2 >0):
        if ls_2[count_2-1] > ls_1[count_1-1]:
            ls_1[count_1+count_2-1] = ls_2[count_2-1]
            count_2 -= 1
        else:
            ls_1[count_1+count_2-1] = ls_1[count_1-1]
            count_1 -= 1
    if count_2 > 0:
        ls_1[:count_2] = ls_2[:count_2]

    print(ls_1)

def main():
    ls_a.sort()
    ls_b.sort()
    #Merge1(ls_a,len(ls_a),ls_b,len(ls_b))
    #Select_M(ls_a,len(ls_a),ls_b,len(ls_b))
    Merge3(ls_a,len(ls_a),ls_b,len(ls_b))

if __name__=='__main__':
    main()