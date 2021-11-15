# from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as say1_hello
from hm_01_测试模块1 import say_hello
# 当两个模块，存在同名函数，那么后导入的模块函数，会覆盖先导入的函数
say_hello()
say1_hello()
