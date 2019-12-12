hello_str = "hello word"

# 1、判断是否以指定字符串开始
#  注意：代码中是字母是严格区分大小写的，两者不等同
print(hello_str.startswith('Hello'))

# 2、判断是否指定字符串结束
print(hello_str.endswith('word'))


# 3、查找指定字符串
# index 同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
# index 如果指定的字符不存在, 会报错
# find 如果指定的字符不存在，则会返回-1
print(hello_str.find("hol"))

# 4、替换字符串
# replace 方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有的字符串的内容
print(hello_str.replace("word", 'python'))
print(hello_str)