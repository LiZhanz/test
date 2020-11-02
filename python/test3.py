# 求s=a+aa+aaa+aaaa+aa···a的值，其中a是一个数字。
# 例如，2+22+222+2222+ 22222（此时共有5个数相加），多少个数相加由键盘输入控制。
def sum1(a,n):
    mysum = 0
    temp = a
    while n>0:
        mysum+=a
        temp*=10
        a=temp+a
        n-=1
    return mysum

# print(sum1(2,6))

# 输入一串字符作为密码，密码只能由数字与字母组成。
# 编写一个函数judge(password),用来求出密码的强度level,根据输入，输出对应密码强度。
# 密码强度判断准则如下（满足其中一条，密码强度增加一级）：○1有数字；○2有大写字母；○3有小写字母；○4位数不少于8位。
def judge(password):
    level = 0
    f1=f2=f3 = True
    for word in password:
        if word.isdigit() and f1:
            level += 1
            f1 = False
        if word.isupper() and f2:
            level += 1
            f2 = False
        if word.islower() and f3:
            level += 1
            f3 = False
    if len(password)>=8:
        level += 1
    return level
                        
# password = input("请输入一个密码：")
# print(judge(password))

# 定义一个lamdba()函数用来求一个数的平方，然后调用该函数求出一个列表所有元素的平方之和。
sqrt1 = lambda x:x**2
def sum2(list1):
    mysum = 0
    for item in list1:
        mysum += sqrt1(item)
    return mysum

a = [x for x in range(1,11)] # 1-10
print(sum2(a))