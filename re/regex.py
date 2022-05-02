"""
regex.py re模塊 功能函數演示
"""
import re


# 目標字符串
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)" #正則表達式

# re模塊調用findall
l = re.findall(pattern,s)
print(l)

# compile 對象調用findall
regex = re.compile(pattern)
l = regex.findall(s,0,12)
print(l)

# 按照正則表達式匹配內容切割字符串
l = re.split(r"[:,]",s)
print(l)

# 替換目標字符串
s = re.subn(r":","-",s)
print(s)

