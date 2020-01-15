#大整数求和

def BigNumberSum(NumA,NumB):
    numA_str = str(NumA)
    numB_Str = str(NumB)
    numA_str = numA_str[::-1]
    numA_str += '0'
    numB_Str = numB_Str[::-1]
    numB_Str += '0'
    maxLength = len(numA_str) > len(numB_Str) and len(numA_str) or len(numB_Str)
    result_ls = [0]*(maxLength+1)
    for i in range(maxLength+1):
        temp = result_ls[i]
        a = 0
        b = 0
        if i < len(numA_str):
            a = int(numA_str[i])
        
        if i < len(numB_Str):
            b = int(numB_Str[i])

        temp = temp + a + b
        if temp >= 10:
            temp = temp - 10
            result_ls[i+1] = 1
        result_ls[i] = temp
    result_ls = result_ls[::-1]
    result = ''
    findFirst = False
    for c in result_ls:
        if not findFirst:
            if c == 0:
                continue
            findFirst = True
        result = result + str(c)
    return result

def main():
    result = BigNumberSum(426709752318,95481253129)
    print(result)

if __name__=='__main__':
    main()