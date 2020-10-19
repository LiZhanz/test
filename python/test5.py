# 编写程序统计该文件内容的行数及单词的个数。
def f1():
    lines=0
    words=0
    with open("res\\zen.txt") as f1:
        for row in f1.readlines():
            lines+=1
            for word in row.split(' '):
                words+=1
    print("行数：",lines,"，单词数：",words)

# 编写程序，用户输入一个目录和文件名，搜索该目录及其子目录中是否存在该文件。
def f2():
    pass

if __name__ == '__main__':
    f1()
    f2()