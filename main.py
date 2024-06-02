import sys

print("請輸入要轉換的文章（結束輸入請按Ctrl+Z+Enter）：")
user_input = sys.stdin.read()
mode = ""
while mode != "1" and mode != "2":
    mode = input("請選擇要寫入的格式(1.覆寫 2.追加):")
mode = "w" if mode == "1" else "a"

with open('main.bf', mode, encoding='utf-8') as f:
    for char in user_input:
        ascii_value = ord(char)
        if ascii_value > 255:
            ascii_value = 42 #如果字符超出ascii255就轉換成"*"
        print(f"{ascii_value}:{chr(ascii_value)}")
        for i in range(ascii_value):
            f.write("+")
        f.write(".[-]")
    print("轉換完成")


        

