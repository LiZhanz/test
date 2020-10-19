import os
import pandas

# 创建一个txt文件，在其中写入学生的基本信息，包括姓名、性别、年龄和电话四个信息。
def f1():
    with open(r"res\test5.txt", 'w') as f:
        f.writelines(','.join(["Tom", "male", "18","1008610010"]))


# 编写程序统计该文件内容的行数及单词的个数。
def f2():
    lines=0
    words=0
    with open(r"res\zen.txt") as f1:
        for row in f1.readlines():
            lines+=1
            for word in row.split(' '):
                words+=1
    print("行数：",lines,"，单词数：",words)

# 编写程序，用户输入一个目录和文件名，搜索该目录及其子目录中是否存在该文件。
def f3():
    dirname=input("请输入目录名：")
    filename=input("请输入文件名")
    for root,dirs,files in os.walk('.'):
        for file in files:
            if file==filename:
                print(filename+"文件在"+os.path.abspath(dirname)+"目录下存在。")
                return
    print(filename + "文件在" + os.path.abspath(dirname) + "目录下不存在。")

# 请编写程序读取该文件内容，并统计每门课程的平均分、最高分和最低分。
def f4():
    table = pandas.read_csv(r"res\score.csv")
    table = table.drop(["考号"],axis=1)
    print("平均分：")
    print(table.mean())
    print("最高分:")
    print(table.max())
    print("最低分：")
    print(table.min())

if __name__ == '__main__':
    # f1()
    # f2()
    f3()
    # f4()