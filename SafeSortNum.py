
def findNearestNumber(numbers):
    index = findTransferPoint(numbers)
    if index == 0:
        return None
    print(numbers)
    number_copy = list.copy(numbers)
    print(number_copy)
    exchangeHead(number_copy,index)
    print(number_copy)
    reverse(number_copy,index)
    print(number_copy)
    return number_copy

def findTransferPoint(numbers):
    for i in range(len(numbers)-1,0,-1):
        if numbers[i] > numbers[i-1]:
            return i
    return 0

def exchangeHead(number,index):
    head = number[index-1]
    for i in range(len(number)-1,0,-1):
        if head < number[i]:
            number[index-1] = number[i]
            number[i] = head
            break
    return number

def reverse(number,index):
    i = index
    j = len(number)-1
    while i < j:
        number[i],number[j] = number[j],number[i]
        i +=1
        j -=1
    return number

def main():
    tets = [1,2,3,4,5]
    tets = findNearestNumber(tets)
    tets = findNearestNumber(tets)
    tets = findNearestNumber(tets)


if __name__ == "__main__":
    main()