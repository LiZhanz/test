# 1.定义一个学生类，
# 类的属性有姓名、年龄、成绩（高等数学、C语言、大学英语）；
# 类方法有获取学生的姓名get_name()，获取学生的年龄get_age()，
# 返回3门科目中最高的分数get_course()。
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        myMax = self.course[0]
        for item in self.course:
            if item > myMax:
                myMax = item
        return myMax

# 2.设计一个向量类，
# 类属性包含向量维数和向量，
# 类方法包括向量的加法、减法、向量与标量的乘法以及两个向量的点乘运算。
# 两个维度不同的向量运算应当返回错误信息。
class Vector:
    def __init__(self,data):
        self.data = data
        self.dim = len(data)
    # 获取向量维度
    def getDim(self):
        return self.dim
    # 向量加法
    def add(self,v):
        res = [0 for x in range(self.dim)]
        if self.dim == v.dim:
            for i in range(self.dim):
                res[i] = self.data[i]+v.data[i]
        else:
            res = None
        return res
    # 向量减法
    def sub(self,v):
        res = [0 for x in range(self.dim)]
        if self.dim == v.dim:
            for i in range(self.dim):
                res[i] = self.data[i] - v.data[i]
        else:
            res = None
        return res
    # 向量和标量的乘法
    def mul(self,v):
        res = [0 for x in range(self.dim)]
        for i in range(self.dim):
            res[i] = self.data[i] * v
        return res
    # 点乘
    def dotMul(self,v):
        res = 0
        if self.dim == v.dim:
            for i in range(self.dim):
                res += self.data[i] * v.data[i]
        return res
    def __str__(self):
        return str(self.data)
if __name__ == '__main__':
    stu = Student("xiaoming",16,[11,22,33])
    print(stu.get_name(),stu.get_age(),stu.get_course())

    # v1 = Vector([1,2,1])
    # v2 =Vector([2,3,1])
    # print("{} + {} = {}".format(v1, v2, v1.add(v2)))
    # print("{} - {} = {}".format(v1,v2,v1.sub(v2)))
    # print("{} * {} = {}".format(v1, 2, v1.mul(2)))
    # print("{} * {} = {}".format(v1, v2, v1.dotMul(v2)))

