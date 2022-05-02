"""
編寫街口函數 從終端輸入端口名稱獲取端口運行狀態中的地址值

思路分析:
1.根據輸入的端口名稱找到對應段落
2.在該段落中匹配address
"""
import re




def get_adress(port):
    f = open("exc.txt")
    while True:
        # 獲取一段內容
        data = ""
        for line in f:
            if line == "\n":
                break
            data += line
        # data為空說明到了文檔結尾
        if not data:
            break

        obj = re.match(port,data) #匹配開始位置
        # obj不為None data就是目標段落
        if obj:
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj = re.search(pattern,data)
            return obj.group()
    return "沒有該端口"

if __name__ == '__main__':
    port = input("端口:")
    print(get_adress(port))

