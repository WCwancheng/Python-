#如何求解最大金矿问题
#解题思路=>背包问题（动态规划）=自低向上求解
#确定全局最优解和最优子结构之前的关系=>状态转移方程式

def MaxGold(w,p,g):
    results = [0]*(w+1)
    for i in range(1,len(g)+1):
        j = w
        while j >=1:
            a = p[i-1]
            if j >= a:
                results[j] = results[j] > (results[j-a] + g[i-1]) and results[j] or (results[j-a] + g[i-1])
            j -= 1
    return results[w]

def main():
    p = [5,5,3,4,3]
    g = [400,500,200,300,350]
    print(MaxGold(7,p,g))

if __name__ == "__main__":
    main()