#! /usr/bin/python
# -*- coding: UTF-8 -*-

from collections import deque

ver = 'python 3.5.4'
print(" こんにちわ　%s" % ver)

# 位置参数
print("{0} is {1} years old".format("Wilber", 28))
print("{} is {} years old".format("Wilber", 28))
print("Hi, {0}! {0} is {1} years old".format("Wilber", 28))

# 关键字参数
print("{name} is {age} years old".format(name="Wilber", age=28))

# 下标参数
li = ["Wilber", 28]
print("{0[0]} is {0[1]} years old".format(li))

# 填充与对齐
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{:>8}'.format('3.14'))
print('{:<8}'.format('3.14'))
print('{:^8}'.format('3.14'))
print('{:0>8}'.format('3.14'))
print('{:a>8}'.format('3.14'))

# 浮点数精度
print('{:.4f}'.format(3.1415926))
print('{:0>10.4f}'.format(3.1415926))

# 进制
# b、d、o、x分别是二进制、十进制、八进制、十六进制
print('{:b}'.format(11))
print('{:d}'.format(11))
print('{:o}'.format(11))
print('{:x}'.format(11))
print('{:#x}'.format(11))
print('{:#X}'.format(11))

# 千位分隔符
print('{:,}'.format(15700000000))

# 注意r前缀
print('c:\some\new')
print(r'c:\some\new')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print(len(text))

# list
squares = [1, 4, 9, 16, 25]
print(squares)
squares2 = squares[:3]
print(squares2)
squares2[0] = 2
print(squares)
print(squares2)

'''
在迭代过程中修改迭代序列不安全
（只有在使用链表这样的可变序列时才会有这样的情况）。
如果你想要修改你迭代的序列（例如，复制选择项），你可以迭代它的复本。
使用切割标识就可以很方便的做到这一点:
'''
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# list methods
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)

# 利用list的append及pop方法将list作为堆栈使用

# 要实现队列，使用 collections.deque，它为在首尾两端快速插入和删除而设计
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

# 列表推导式
squares1 = list(map(lambda x: x ** 2, range(10)))
# 又は
squares2 = [x ** 2 for x in range(10)]
squares3 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares3)

# 集合推导式语法
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def my_print(args):
    print(args)


def move(n, a, b, c):
    my_print((a, '-->', c)) if n == 1 else (
        move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))


move(3, 'a', 'b', 'c')
