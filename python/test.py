import re

# 有一段英文文本，其中有单词连续重复了2次，编写程序检查重复的单词并只保留一个。
def f1():
    x = 'This is a a desk.'
    pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
    matchResult = pattern.search(x)
    x = x.replace(matchResult.group(0),matchResult.group(1))
    print(x)

# 编写程序，用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。
def f2():
    x = 'This is  abc a big big desk.'
    pattern = re.compile(r'\b\w{3}\b')
    matchResult = pattern.search(x)
    words = pattern.findall(x)
    print(words)

# 使用正则表达式清除字符串中的HTML标记。
def f3():
    x = "<h1>hello world</h1> <p>pppppp</p> <img src='' />"
    pre = re.compile('>(.*?)<')
    s1 = ''.join(pre.findall(x))
    print(s1) 

# 假设有一段英文，其中有单独的字母I误写为i，编写程序进行纠正。
def f4():
    x = 'i am a zzizz,i am happy.'
    pattern = re.compile(r'\b(i\s){1,}\b')
    matchResult = pattern.search(x)
    x = x.replace(matchResult.group(0),"I ")
    print(x)

if __name__ == "__main__":
    # f1()
    # f2()
    # f3()
    f4()
