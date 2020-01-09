import tkinter as tk
from decimal import Decimal

root = tk.Tk()
root.title("计算器")
root.resizable(0,0)
global vartext
current_cal_type = ''
last_text = '0'
cur_back = False

vartext = tk.StringVar()
class Calculator_Control:
    an_niu = ''
    result = '0'
    cur_in = []
    cur_is_x = False

    def __init__(self,an):
        self.an_niu = an
    
    def ClickBtn(self):
        if self.an_niu == '':
            print("没有操作，点击为空")
            return

        if self.an_niu in ['0','1','2','3','4','5','6','7','8','9','.']:
            self.__SelectNum()
        elif self.an_niu in ['+','-','x','÷','%']:
            self.__SelectCalculatorType()
        elif self.an_niu == 'AC':
            self.__Clear()
        elif self.an_niu == '+/-':
            self.__ChangeZF()
        elif self.an_niu == '←':
            self.__FallBack()
        elif self.an_niu == '=':
            self.__GetResult()
        
        self.__ShowVartext()

    #选择数字
    def __SelectNum(self):
        global cur_back
        if self.an_niu == '.' and self.cur_is_x:
            print("1111")
        
        elif self.cur_in == [] and self.an_niu == '0':
            print("0000")
            return
        else:
            self.cur_is_x = True
            self.cur_in.append(self.an_niu)

        cur_back = True
        self.result = ''.join(self.cur_in)

    #点击算法操作符
    def __SelectCalculatorType(self):
        if self.cur_in == []:
            return
            
        global current_cal_type,last_text
        self.__GetResult()
        current_cal_type = self.an_niu
        last_text = ''.join(self.cur_in)
        self.cur_in.clear()
        self.result = last_text

    #清除操作
    def __Clear(self):
        global current_cal_type,last_text
        current_cal_type = ''
        self.cur_in.clear()
        self.result = '0'

    #转换正负操作
    def __ChangeZF(self):
        if self.cur_in == []:
            return

        if self.cur_in[0] == '-':
            self.cur_in.pop(0)
        else:
            self.cur_in.insert(0,'-')
        self.result = ''.join(self.cur_in)

    #回退一步操作数字的时候有用，点击了算法操作不起作用       
    def __FallBack(self):
        global cur_back
        print(cur_back)
        print(self.cur_in)
        if cur_back and self.cur_in != []:
            length = len(self.cur_in)
            self.cur_in.pop(length-1)
            if length == 1:
                self.result = '0'
            elif length == 2 and self.cur_in[0] == '-':
                self.result = '0'
            else:
                self.result = ''.join(self.cur_in)
        else:
            self.result = '0'

    #计算结果，显示结果，清除相关操作
    def __GetResult(self):  
        global current_cal_type,last_text,cur_back
        cur_back = False
        current_text = ''.join(self.cur_in)
        if current_cal_type == '':
            self.result = current_text
        else: 
            if current_cal_type == '+':
                self.result = str(Decimal(last_text) + Decimal(current_text))
            elif current_cal_type == '-':
                self.result = str(Decimal(last_text) - Decimal(current_text))
            elif current_cal_type == 'x':
                self.result = str(Decimal(last_text) * Decimal(current_text))
            elif current_cal_type == '÷':
                self.result = str(Decimal(last_text) / Decimal(current_text))
            elif current_cal_type == '%':
                self.result = str(Decimal(last_text) % Decimal(current_text))
            
        current_cal_type = ''
        self.cur_in.clear()
        self.cur_in.append(self.result)
        print("last_text = %s" % last_text)
    
    #显示结果
    def __ShowVartext(self):
        print("显示结果 %s " % self.result)
        if len(self.result) <=15:
            vartext.set(self.result)
        else:
            vartext.set("{0:.15f}".format(float(self.result)).rstrip('0'))

   

def Calculator_UI(): 
    global vartext
    entry1 = tk.Label(root,width=25, height=3, bg='white', anchor='se', textvariable=vartext)
    entry1.grid(row=0, columnspan=4)
    vartext.set(str(0))
    
    Create_Btn(' AC ','AC',1,0)
    Create_Btn(' +/- ','+/-',1,1)
    Create_Btn(' % ','%',1,2)
    Create_Btn(' ÷ ','÷',1,3)

    Create_Btn(' 7 ','7',2,0)
    Create_Btn(' 8 ','8',2,1)
    Create_Btn(' 9 ','9',2,2)
    Create_Btn(' x ','x',2,3)

    Create_Btn(' 4 ','4',3,0)
    Create_Btn(' 5 ','5',3,1)
    Create_Btn(' 6 ','6',3,2)
    Create_Btn(' - ','-',3,3)

    Create_Btn(' 1 ','1',4,0)
    Create_Btn(' 2 ','2',4,1)
    Create_Btn(' 3 ','3',4,2)
    Create_Btn(' + ','+',4,3)

    Create_Btn(' 0 ','0',5,0)
    Create_Btn(' . ','.',5,1)
    Create_Btn(' ← ','←',5,2)
    Create_Btn(' = ','=',5,3)


def Create_Btn(text1,text2,r,c): 
    btn = tk.Button(root,text = text1,bg='white',fg='black',width = 5,height = 2,command=Calculator_Control(text2).ClickBtn)
    btn.grid(row = r,column = c)

def main():
    Calculator_UI()

main()
root.mainloop()

