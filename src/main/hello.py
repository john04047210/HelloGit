#! /usr/bin/python
# -*- coding: UTF-8 -*-

ver = 'python 3.5.4'
print(" こんにちわ　%s" %ver)

# 位置参数
print("{0} is {1} years old".format("Wilber", 28))
print("{} is {} years old".format("Wilber", 28))
print("Hi, {0}! {0} is {1} years old".format("Wilber", 28))

# 关键字参数
print("{name} is {age} years old".format(name = "Wilber", age = 28))

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


def my_print(args):
    print(args)


def move(n, a, b, c):
    my_print((a, '-->', c)) if n == 1 else (move(n-1, a, c, b) or move(1, a, b, c) or move(n-1, b, a, c))

move(3, 'a', 'b', 'c')