#冒泡排序 O(n^2)
def MaoPaoSort(ls):
    for i in range(len(ls)):
        for j in range(i + 1,len(ls)):
            if ls[i] > ls[j]:
                ls[i],ls[j]=ls[j],ls[i]
#选择排序 O(n^2)
def SelectSort(ls):
    for i in range(len(ls)):
        index = i
        for j in range(i+1,len(ls)):
            if ls[index] > ls[j]:
                index = j

        ls[index],ls[i]=ls[i],ls[index]

#快速排序 时间O(nlog2n) 空间O(nlog2n)
def QuickSort(ls,low,high):
    if low < high:
        pivot = ls[high] #标志元素
        index = low - 1
        for i in range(low,high):
            if ls[i] <= pivot:
                index = index + 1
                ls[index],ls[i] = ls[i],ls[index]
                
        ls[high],ls[index+1] = ls[index+1],ls[high]

        QuickSort(ls,low,index-1)
        QuickSort(ls,index+1,high)

#归并 
def Merge(ls,low,mid,high):
    l_count = mid - low + 1
    r_count = high - mid
    ls_l = [0] * (l_count)
    ls_r = [0] * (r_count)
    for i in range(0,l_count):
        ls_l[i] = ls[low + i]
    
    for j in range(0,r_count):
        ls_r[j] = ls[j + mid + 1]

    l_index = 0
    r_index = 0
    start = low
    while(l_index < l_count and r_index < r_count):
        if ls_l[l_index] <= ls_r[r_index]:
            ls[start] = ls_l[l_index]
            l_index += 1
        else:
            ls[start] = ls_r[r_index]
            r_index += 1

        start += 1

    while l_index < l_count:
        ls[start] = ls_l[l_index]
        l_index += 1
        start += 1
    
    while r_index < r_count:
        ls[start] = ls_r[r_index]
        r_index += 1
        start += 1
    
#归并排序 时间O(nlogn) 空间O(n)
def MergeSort(ls,low,high):
    if low < high:
        mid = int((low + (high-1))/2)
        MergeSort(ls,low,mid)
        MergeSort(ls,mid+1,high)
        Merge(ls,low,mid,high)

ls = [1,3,436,2,54,754,23,6875,32]
def main():
    print(ls)
    # SelectSort(ls)
    MergeSort(ls,0,len(ls)-1)
    print(ls)
    
if __name__=='__main__':
    main()