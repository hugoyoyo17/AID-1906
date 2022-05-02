"""
regex1.py re模塊 功能函數演示2
生成match對象函數
"""

import re

s = "今年是2019年,建國109年"
pattern = r"\d+"

# 返回迭代對象
it = re.finditer(pattern,s)

for i in it:
    print(i.group()) #獲取match對象對應內容

# 完全匹配一個字符串
m = re.fullmatch(r"[,\w]+",s)
print(m.group())

# 匹配開始位置
m = re.match(r"\w+?",s)
print(m.group())

# 匹配第一處符合正則規則的內容
m = re.search(r"\d+",s)
print(m.group())