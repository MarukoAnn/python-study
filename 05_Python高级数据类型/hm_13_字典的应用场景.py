# 使用多个键值对，对存储描述一个 `物体` 的相关信息 -- 描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历
card_list = [{"name": "张三",
              "qq": "123456",
              "phone": "110"},
             {"name": "张三",
              "qq": "123456",
              "phone": "110"
              }]
for card_info in card_list:
    print(card_info)