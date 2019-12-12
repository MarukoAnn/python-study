xm_dict = {'name': '小明',
           'age': 18
           }

# 1、统计键值对的数量

print(len(xm_dict))

# 2、合并字典

tem_dict = {'height': 1.75,
            'age': 20}
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xm_dict.update(tem_dict)

# print(xm_dict)

# 3.清空字典

xm_dict.clear()

print(xm_dict)