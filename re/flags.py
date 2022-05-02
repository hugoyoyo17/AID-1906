"""
flags.py
flags擴展功能展示
"""

import re

s = """Hello 
北京
"""

# 只能匹配ASCII編碼
# regex = re.compile(r"\w+",flags =re.A)

# 不區分大小寫
# regex = re.compile(r"[a-z]+",flags=re.I)

# .可以匹配換行
# regex = re.compile(r".+",flags=re.S)

# ^,$可以匹配每一行開頭結尾位置
# regex = re.compile(r"^北京",flags=re.M)

# 給正則分行註釋
pattern= r"""\w+ # Hello
\s+ # 匹配換行
\w+ # 北京
"""
regex = re.compile(pattern,flags= re.X|re.I)

l = regex.findall(s)
print(l)