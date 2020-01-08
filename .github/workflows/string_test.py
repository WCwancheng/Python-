
# -*- coding: utf-8 -*-
import os
import string


str_t = "我是?! ,m字M是我"

def string_fazhuan1():
    print(str_t)
    print(str_t[::-1])

def string_isHuiWen(str_t):
    print(string.punctuation)
    str_hui = str_t
    str_hui = str_hui.lower().replace(' ','')
    for char in string.punctuation:
        if char in str_hui:
            str_hui = str_hui.replace(char,'')
    print(str_hui)
    str_t = str_hui[::-1]
    print(str_t)
    if str_hui == str_t:
        print("这是回文字符串")
    else:
        print("不是回文字符串")

def string_fazhuan2():
    print(str_t)
    list_str = list(str_t)
    print(list_str)
    list_str.reverse() #列表的reverse反转不具有返回值
    print(list_str)
    str_2 = ''.join(list_str)
    print(str_2)
    

def main():
    #string_fazhuan1()
    string_fazhuan2()
    string_isHuiWen(str_t)

if __name__=='__main__':
    main()