# 一球从100m高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 弹跳次数
n = 10
ms = 100 
high = 100
while n>1:
    ms+=high
    high/=2
    n-=1
print("共经过了{:.4f}米，第10次反弹{:.4f}米".format(ms,high/2))

# 编写程序，产生两个0~100之间（包含0和100）的随机整数RND1和RND2，求这两个整数的最大公约数和最小公倍数。
# import random
# rnd1 = random.randint(0,100)
# rnd2 = random.randint(0,100)
# print("两个随机数是：{},{}".format(rnd1,rnd2))
# if rnd1==0 or rnd2==0:
#     print("结束")
#     exit
# maxRnd = max(rnd1,rnd2)
# minRnd = min(rnd1,rnd2)
# temp = minRnd
# while True:
#     if temp%rnd1==0 and temp%rnd2==0:
#         print("最小公倍数是：{}".format(temp))
#         break
#     temp+=1
# temp = minRnd
# while True:
#     if rnd1%temp==0 and rnd2%temp==0:
#         print("最大公因数是：{}".format(temp))
#         break
#     temp-=1

# 编写程序，根据输入的点的横坐标和纵坐标，输出该点所在的象限。
# x = eval(input('请输入x：'))
# y = eval(input('请输入y：'))
# temps = [3,-2,-12,-7,1,-4,2,-8,0]
# temp2str = ['第一象限','第二象限','第三象限','第四象限','X正半轴','X负半轴','Y正半轴','Y负半轴','原点']
# dict1 = dict(zip(temps,temp2str))
# temp = 0
# if x>0:
#     temp+=1
# elif x<0:
#     temp+=-4
# if y>0:
#     temp+=2
# elif y<0:
#     temp+=-8
# print(dict1[temp])


# 编写程序，判断用户输入的字符是数字字符、字母字符还是其他字符。
# char = input("请输入字符：")
# if char.isdigit():
#     print("输入的是数字字符")
# elif char.isalpha():
#     print("输入的是字母字符")
# else:
#     print("输入的是其他字符")