
import datetime

def Age():
    birth_day = int(input("请输入你的出生日期 "))
    age = datetime.date.today().year - birth_day
    print("你好xxx,你今年\033[41m %d \033[0m岁" % age)

def main():
    Age()

if __name__=='__main__':
    main()