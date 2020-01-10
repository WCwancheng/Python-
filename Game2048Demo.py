import tkinter as tk
import random

global vartext,game_ctrl,max_vartext,max_result,btn_vartext
root = tk.Tk()
root.title("2048")
root.resizable(0,0)
vartext = tk.StringVar()
max_vartext = tk.StringVar()
rect_ls = [0]*(16)
max_result = 0
btn_vartext = tk.StringVar()

class GameState:
    NONE = 0
    START = 1
    GAMEING = 2
    END = 3

class Game_Ctrl:
    game_state = GameState.NONE
    cur_ls = [0]*(16)
    cur_empty_ls = []
    result = 0

    def __init__(self,state):
        self.game_state = state

    #键盘按键监听
    def GameKeyCall(self,event):
        if self.game_state != GameState.GAMEING:
            return
        
        if event == 'Up':
            self.MergeRectUp()
        elif event == 'Down':
            self.MergeRectDown()
        elif event == 'Right':
            self.MergeRectRight()
        elif event == 'Left':
            self.MergeRectLeft()
        else:
            print("按下了不可操作按钮")
            return

    def MergeRectUp(self):
        print("进来开始合并 向上合并")
        length = len(self.cur_ls)
        for i in range(length-4):
            if i + 4 <= length - 1:
                if self.cur_ls[i] == self.cur_ls[i+4]:
                    self.MergeSwap1(i,i+4)
                elif self.cur_ls[i] == 0 and self.cur_ls[i+4] > 0:
                    self.MergeSwap2(i,i+4)
        self.CreateNum()
    
    def MergeRectDown(self):
        print("进来开始合并 向下合并")
        length = len(self.cur_ls)
        for i in range(length-1,0,-1):
            if i -4 >= 0:
                if self.cur_ls[i] == self.cur_ls[i-4]:
                    self.MergeSwap1(i,i-4)
                elif self.cur_ls[i] == 0 and self.cur_ls[i-4] > 0:
                    self.MergeSwap2(i,i-4)
        self.CreateNum()
    
    def MergeRectRight(self):
        print("进来开始合并 向右合并")
        length = len(self.cur_ls)
        for i in range(length-1,0,-1):
            if i % 4 != 0:
                if self.cur_ls[i] == self.cur_ls[i-1] and i%4 != (i-1)%4:
                    self.MergeSwap1(i,i-1)
                elif self.cur_ls[i] == 0 and self.cur_ls[i-1] > 0:
                    self.MergeSwap2(i,i-1)
        self.CreateNum()

    def MergeRectLeft(self):
        print("进来开始合并 向左合并")
        length = len(self.cur_ls)
        for i in range(length):
            if i % 4 != 3:
                if self.cur_ls[i] == self.cur_ls[i+1] and i%4 != (i+1)%4:
                    self.MergeSwap1(i,i+1)
                elif self.cur_ls[i] == 0 and self.cur_ls[i+1] > 0:
                    self.MergeSwap2(i,i+1)
        self.CreateNum()

    def MergeSwap1(self,index,wapIndex):
        self.result += self.cur_ls[index]
        self.cur_ls[index] = self.cur_ls[index] * 2
        self.cur_ls[wapIndex] = 0
    
    def MergeSwap2(self,index,wapIndex):
        self.cur_ls[index] = self.cur_ls[wapIndex]
        self.cur_ls[wapIndex] = 0

    def StartGame(self):
        if self.game_state != GameState.NONE:
            return
        
        self.result = 0
        self.cur_ls = [0]*(16)

        self.game_state = GameState.START
        #随机生成两位数字
        self.CreateNum()
        self.CreateNum()
        self.game_state = GameState.GAMEING
        global btn_vartext
        btn_vartext.set("游戏中...")
        print("开始游戏")

    #生成一个数字
    def CreateNum(self):
        self.cur_empty_ls.clear()
        for i in range(len(self.cur_ls)):
            if self.cur_ls[i] == 0:
                self.cur_empty_ls.append(i)
        
        rad = random.randint(0,100)
        num = rad >= 50 and 4 or 2
        print(num)
        #插入到一个位置中
        empty_len = len(self.cur_empty_ls)

        index = 0
        if empty_len > 0:
            index = random.randint(0,empty_len-1)
        else:
            self.GameOver()
            return

        pos = self.cur_empty_ls[index]
        self.cur_ls[pos] = num
        self.ShowUIText()

    def ShowUIText(self):
        global vartext,rect_ls
        print(self.cur_empty_ls)
        print(self.cur_ls)
        for i in range(len(self.cur_ls)):
            if self.cur_ls[i] != 0:
                rect_ls[i].set(str(self.cur_ls[i]))
            else:
                rect_ls[i].set('')
        self.ShowResult()

    def GameOver(self):
        self.game_state = GameState.END
        print("游戏结束")
        self.ShowResult(True)
        self.game_state = GameState.NONE
        global btn_vartext
        btn_vartext.set("再来一局")

    def ShowResult(self,isOver=False):
        global vartext,max_vartext,max_result
        str_text = "当前游戏分数: %d " % self.result
        if isOver:
            str_text = "游戏结束，总共获得分数: %d " % self.result
            if self.result > max_result:
                max_result = self.result
                max_vartext.set("历史最高分: %d " % max_result)
        vartext.set(str_text)


def CreateUI():
    global vartext,rect_ls,max_vartext,max_result
    print("生成UI")
    entry1 = tk.Label(root,fg='black',width=25, height=3, bg='white', anchor='se', textvariable=vartext)
    entry1.grid(row=0, columnspan=4)
    vartext.set("是兄弟，就赶紧来玩一把！！！")

    entry1 = tk.Label(root,fg='black',width=25, height=2, bg='white', anchor='se', textvariable=max_vartext)
    entry1.grid(row=5, columnspan=4)
    max_vartext.set("历史最高分: %d " % max_result)
    
    for i in range(16):
        vartext1 = tk.StringVar()
        rect_ls[i] = vartext1
        btn = tk.Button(root,textvariable=vartext1,bg='white',fg='black',width = 5,height = 2)
        btn.grid(row = int((i/4)+1),column = int(i%4))

    CreateBtn()

def CreateBtn():
    global btn_vartext
    btn_gameStart = tk.Button(root,textvariable=btn_vartext,bg='white',fg='black',width = 11,height = 2,command=game_ctrl.StartGame)
    btn_gameStart.grid(row = 6,column = 1,columnspan = 2)
    btn_vartext.set(str("开始游戏"))

def KeyCall(event):
    game_ctrl.GameKeyCall(event.keysym)    

def main():
    CreateUI()
    


game_ctrl = Game_Ctrl(GameState.NONE)
main()
root.bind("<Key>",KeyCall)
root.focus_set()
root.mainloop()