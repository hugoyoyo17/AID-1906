"""
regex2.py
match 對象屬性演示
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefghi") #match對象

# 屬性變量
print(obj.pos) #目標字符串開始位置
print(obj.endpos) #目標字符串結束位置
print(obj.re) #正則
print(obj.string) #目標字符串
print(obj.lastgroup) #最後一組組名
print(obj.lastindex) #最後一組序列號

print("==========================")
print(obj.span()) #匹配內容在字符串中位置
print(obj.start())
print(obj.end())
print(obj.groupdict()) #生成捕獲組字典
print(obj.groups()) #子組對應內容元組
print(obj.group()) #獲取match對象對應內容
print(obj.group("pig"))