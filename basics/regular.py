#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Email         : huangtao@yimian.me
# * Create time   : 2018/5/20 下午5:37
# * Last modified : 2018/5/20 下午5:37
# * Filename      : regular.py
# * Description   : 1、介绍^ . * $的用法
#                   1）^ 匹配输入字符串开始的位置。
#                   2）. 匹配除换行符 \n 之外的任何单字符。
#                   3）* 匹配前面的子表达式零次或多次。
#                   4）$ 匹配输入字符串的结尾位置。
# **********************************************************

import re

###################一##################

# 需要匹配的字符串
line = "huang123"

# 1.匹配以h开头的内容
if re.match("^h", line):
    print "1.匹配以h开头的内容"

# 2.以h开头，后面跟着任意一个字符串
if re.match("^h.", line):
    print "2.以h开头，后面跟着任意一个字符串"

# 3.以h开头，后面跟着任意数量的字符串
if re.match("^h.*", line):
    print "3.以h开头，后面跟着任意数量的字符串"

# 4.以3结尾
if re.match(".*3$", line):
    print "4.以3结尾"

# 5.以h开头，以3结尾，中间只有任意一个字符串
if re.match("^h.3$", line):
    print "5.以h开头，以3结尾，中间只有任意一个字符串"

# 6.以h开头，以3结尾，中间可以存在任意数量的字符串
if re.match("^h.*3$", line):
    print "6.以h开头，以3结尾，中间可以存在任意数量的字符串"

###################一##################
# 1）()标记一个子表达式的开始和结束位置。
# 2）?匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。

line = "ahuuhhaaahang123"
# 我要获取huuh

match_obj = re.match(".*(h.*h).*", line)
if match_obj:
    print "1.使用()只获取括号里面的值"
    print match_obj.group(1)

match_obj = re.match(".*?(h.*h).*", line)
if match_obj:
    print "2.使用非贪婪限定符?强制从左开始匹配"
    print match_obj.group(1)

match_obj = re.match(".*?(h.*?h).*", line)
if match_obj:
    print "3.使用非贪婪限定符?强制从左开始匹配，遇到第一个h就停止匹配"
    print match_obj.group(1)

# 说明
# 1、输出结果为haaah，我们发现它默认是反向获取，从右边开始，获取到haaah就停止
# 2、输出结果为huuhhaaah，当我们在前面加上？，它确实从左开始匹配，但是会一直匹配到最后一个h
# 3、输出结果为huuh，从左开始匹配，并且遇到第一个h就停止匹配


###################一##################
# 1）+匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
# 2）{n} n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
# 3）{n,} n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
# 4）{n,m} m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。

# 需要匹配的字符串
line = "ahuuhhaaahhhang123"

# 1.获取h和h之间需要包含特定数量字符的字符串，使用+，h和h之间至少要有一个字符
match_obj = re.match(".*(h.+h).*", line)
if match_obj:
    print "1.使用+，h和h之间至少要有一个字符"
    print match_obj.group(1)

# 2.使用{1}，h和h之间至少要有一个字符
match_obj = re.match(".*(h.{1}h).*", line)
if match_obj:
    print "2.使用{1}，h和h之间至少要有一个字符"
    print match_obj.group(1)

# 3.使用{2,}，h和h之间至少要有2个字符
match_obj = re.match(".*(h.{2,}h).*", line)
if match_obj:
    print "3.使用{2,}，h和h之间至少要有2个字符"
    print match_obj.group(1)

# 4.使用{3,5}，h和h之间字符限定在3到5个字符
match_obj = re.match(".*(h.{3,5}h).*", line)
if match_obj:
    print "4.使用{3,5}，h和h之间字符限定在3到5个字符"
    print match_obj.group(1)



###################一##################
# 1）｜指明两项之间的一个选择。
# 2）[123] 只要是123中的其中一个即可。
# 3）[0-9] 只要是0-9中的任意数字即可。
# 4）[^1] 非，只要不是1即可。


# 需要匹配的字符串
line = "huang123"
#
match_obj = re.match("(huang123|123qwe)", line)
if match_obj:
    print match_obj.group(1)

#
line = "18858118888"

