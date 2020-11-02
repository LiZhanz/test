# -*- coding: utf-8 -*-

# 5 
def no5():
    I = eval(input("请输入当月利润："))
    P = 0
    if I>100:
        P += (I-100)*0.01
        I = 100
    if I>60:
        P += (I-60)*0.015
        I = 60
    if I>40:
        P += (I-40)*0.03
        I = 40
    if I>20:
        P += (I-20)*0.05
        I = 20
    if I>10:
        P += (I-10)*0.075
        I = 10
    if I<=10:
        P += I*0.1
    print("当月奖金为{}万元".format(P))
    

# 4 输入某年某月某日，判断这一天是这一年的第几天。
def no4():
    year = eval(input("请输入年份："))
    month = eval(input("请输入月份："))
    day = eval(input("请输入日："))
    if year%4==0 and year%1000!=0:
        two = 29
    else:
        two = 28
    months = [31,two,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(month-1):
        days += months[i]
    days += day

    print("{}年{}月{}日是{}年的第{}天".format(year,month,days,year,days))

# 3 输入三个整数x、y、z，请把三个数由小到大输出。
def no3():
    x = int(input("请输入x："))
    y = int(input("请输入y："))
    z = int(input("请输入z："))
    if x>y:
        x,y = y,x
    if x>z:
        x,z = z,x
    if y>z:
        y,z = z,y
    
    print("从小到大排序：{} {} {}".format(x,y,z))

# 2 输入三角形的三条边，判断是否能组成三角形，若能，计算三角形的面积。
def no2():
    import math
    num1 = eval(input("请输入第一条边长："))
    num2 = eval(input("请输入第二条边长："))
    num3 = eval(input("请输入第三条边长："))
    if num1<=0 or num2<=0 or num3<=0:
        print("输入不合法")
        
    elif num1+num2>num3 and num1+num3>num1 and num2+num3>num1:
        print("不能组成三角形")
    else:
        p = (num1+num2+num3)
        temp = p*(p-num1)*(p-num2)*(p-num3)
        print("能组成三角形，面积为：{}".format(math.sqrt(temp)))

# 1 编写一个程序，判断用户输入的字符是数字字符，字母字符1还是其他字符。
def no1():
    str1 = input("请输入一个字符：\n")
    if str.isdigit(str1):
        print("digit")
    elif str.isalpha(str1):
        print("alpha")
    else:
        print("other")    

if __name__ == "__main__":
    no5()