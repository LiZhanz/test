import re

# 有一段英文文本，其中有单词连续重复了2次，编写程序检查重复的单词并只保留一个。
def f1():
    str = "This is is a dest."
    pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
    matchResult = pattern.search(str)
    str = pattern.sub(matchResult.group(1),str)
    print(str)
    print(matchResult.group(0))

def f2():
    x = 'This is a a desk.'
    pattern = re.compile(r'(?P<f>\b\w+\b)\s(?P=f)')
    matchResult = pattern.search(x)
    x = x.replace(matchResult.group(0),matchResult.group(1))
    print(x)
if __name__ == "__main__":
    f1()
    f2()
