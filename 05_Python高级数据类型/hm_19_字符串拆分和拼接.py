# 假设: 以下内容是从网络上抓取的
# 要求:
# 1. 将字符串中的空白字符全部去掉
# 2. 在使用 " " 作为分隔符, 拼接成一个整齐的字符串
poem_str = "登黄鹤楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\n 更上一层楼"
print(poem_str)

# 1.拆分字符串

poem_list = poem_str.split()
print(poem_list)

# 2. 合并字符串
result = " ".join(poem_list)
print(result)