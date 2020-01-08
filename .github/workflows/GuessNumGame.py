import random

class GuessData():
    level_ls = [100,1000,10000,100000]
    select_level = 1
    game_num = 0

def selectLevel():
    print("这是一个猜数字的游戏，尝试一下你要猜多少次猜到最后的结果")
    print("输入\033[41m 1 \033[0m为低级 1-100 ")
    print("输入\033[41m 2 \033[0m为低级 1-1000 ")
    print("输入\033[41m 3 \033[0m为低级 1-10000 ")
    print("输入\033[41m 4 \033[0m为低级 1-100000 ")
    level = int(input("请输入要游戏的级别"))
    GuessData.select_level = level

def getResult():
    level_num = GuessData.level_ls[GuessData.select_level-1]
    GuessData.game_num = random.randint(1,level_num+1)

#猜数字大小游戏
def Guess():
    gameOver = True
    print("游戏开始，请开始你的表演")
    game_count = 0
    game_num = GuessData.game_num
    while gameOver:
        num = int(input("请输入你要猜的整数"))
        if num > game_num:
            print("比结果大了一点喔，快接近真相了，加油。。。")
        elif num < game_num:
            print("比结果小了一点喔，快接近真相了，加油。。。")
        else: 
            print("恭喜你猜对了，总共猜了\033[41m %d \033[0m" % game_count)
            gameOver = False
            break
        game_count += 1

def main():
    selectLevel()
    getResult()
    Guess()

if __name__=='__main__':
    main()