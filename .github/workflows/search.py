#线性查找 时间O(n) 空间O(1)
def LineSearch(ls,value):
    for i in range(len(ls)):
        if ls[i] == value :
            return i
    return -1

#二分查找,不递归 时间O(logn) 空间O(1)
def BinarySearch1(ls,value):
    length = len(ls)
    r = length - 1
    l = 0
    count = 0
    while True:
        if r >= l:
            count += 1
            #先求中间值
            mid = int(l + (r-l)/2)
            #判断在中间还是左边还是右边
            if value == ls[mid]:
                print("查找了多少次 %d " % count)
                return mid
            elif value < ls[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            return -1

#二分查找，递归 时间O(1) 空间O(longn)
def BinarySearch2(ls,value,r,l):
    if r >= l:
        mid = int(l + (r - l)/2)
        if value == ls[mid]:
            return mid
        elif value < ls[mid]:
            return BinarySearch2(ls,value,mid - 1,l)
        else:
            return BinarySearch2(ls,value,r,mid + 1)
    else:
        return -1

ls = [1,3,436,2,54,754,23,6875,32]
def main():
    value = 54
    ls.sort()
    print(ls)
    #index = LineSearch(ls,value) 线性查找
    #index = BinarySearch1(ls,value) #二分查找不递归
    r = len(ls) - 1
    l = 0
    index = BinarySearch2(ls,value,r,l) #二分查找不递归
    if index == -1:
        print("列表中不存在该数值")
    else:
        print("列表中改数值的下标为: %d " % index)

if __name__=='__main__':
    main()
