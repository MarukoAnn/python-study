## python 基础学习
### 1、变量的定义
- 可以使用其他变量的计算结果来定义
###  2、变量的类型
- 在内存中创建变量，会包括：
   - 1、变量的名称
   - 2、变量的数据
   - 3、变量的存储数据的类型
   - 4、变量的地址
### 3、python中数据的类型
- 数据类型可分为数据型和 非数据型
   - 数据型
        - 整型(int)
        - 浮点型(float)
        - 布尔型(bool)
           - 真 True 非 0 数 --- 非零即真
           - 假 Folse 0
        - 复数型(complex)
           - 主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题
   - 非数据型
      - 字符串
      - 列表
      - 元组
      - 字典
- 注意：使用 type 函数可以查看一个变量的类型
### 4、不同的类型变量之间的计算
- 1)、数字型变量之间可以直接计算
   - 在Python 中, 两个数字型变量可以直接进行算数运算的
   - 如果变量bool 型, 在计算时
      - True 对应的数字时 1
      - False 对应的数字时 0
- 2)、字符串变量之间使用 + 拼接字符串
   - 在Python中, 字符串之间可以使用 + 拼接生成新的字符串
- 3)、字符串变量 可以和整数 使用 * 重复凭借相同的字符串
- 4)、数字型变量 和 字符串之间不能进行其他计算
### 5、变量的输入
- 所谓输入，就是用代码获取用户通过键盘输入的信息
- 例如: 去银行取钱，在ATM上输入密码
- 在Python中，如果需要获取用户在键盘上的输入信息，需要使用到input函数
##### 1)、关于函数
   - 一个提前准备号的功能(别人或者自己写的代码), 可以之际使用，而不用关心内部细节
   - 目前已经嘘唏过的函数  
      - print(x) 将x输出到控制台
      - type(x) 查看x的变量类型
##### 2)、input 函数实现键盘输入
- 在Python 中可以使用 input 函数从键盘等待用户的输入
- 在用户输入任何内容Python 都认为这是一个字符串
- 语法如下：
```
字符串变量 = input("提示信息：")
```
##### 3)、类型转换函数
- 1、int(x) 将x转为一个整数
- 2、float(x) 将x转换到一个浮点数
##### 4)、变量的格式化输出
- 在Python中可以使用print 函数将信息输出到控制台
- 如果希望输出的文字信息的同时，一起输出数据，就需要使用到**格式化操作符**
- % 被称为 **格式化操作符** 、专门用于处理字符串中的格式
   - 包含 % 的字符，被称为 **格式化字符串**
   - % 和不同的字符连用，不同类型的数据需要使用不同的格式化字符
- 格式化字符
  - %s：  字符串
  - %d：  有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方用 0 补全
  - %f：  浮点数, %.02f 表示小数点后只显示两位
  - %%：  输出%
- 语法格式如下：
````
print("格式化字符串" % 变量1)
print("格式化字符串" % (变量1, 变量2))
````
### 6、变量的命名
##### 01、标识符和关键字
###### 1.1标识符
- 标识符就是程序员定义的变量名、函数名
- 名字需要有见名知义的效果
   - 标识符可以由字母、下划线 和数字组成
   - 不能以数字开头
   - 不能与关键字重名
###### 1.2 关键字
- 关键字 就是在Python 内部已经使用的标识符
- 关键字具有特殊功能和含义
- 开发者不允许定义和关键字相同的名字的标识符
- 通过以下命令可以查看Python 中的关键字
```
import keyword
print(keyword.kwlist)
```
- import 关键字可以导入一个工具包
- 在Python 中不同的工具包，提供有不同的工具
##### 02 变量的命名规则
- 命名规则可以被视为一种惯例，并无绝对与强制目的时为了增加代码的识别和可读性
- 注意 Python中的标识符是区分大小写的
   - 1、在定义变量时,为了保证代码格式， = 的左右应该各保留一个空格
   - 2、在Python 中，如果变量名需要由两个或者多个单词组成时，可以按照一下方式命名：
      - a、每个单词都使用小写字母
      - b、单词与单词自建使用_ 下划线连接
      - c、例如：first_name、last_name、qq_number、qq_password  
##### 驼峰命名法
- 当变量名是由两个或者多个但粗组成时,还可以利用驼峰命名法来命名
- 小驼峰式命名法
   - 第一个单词以小写字母开始，后续单词的首字母大写
   - 例如：fistName、lastName、cameCase
- 大驼峰式命名法
   - 每一个单词的首字母都采用大写字母
   - 例如： FirstName、LastName、CamelCase
### if语句体验
##### 1、if判断语句的基本语法
- 在Python 中，if 语句就是用来进行判断的，格式如下：
```
if 要判断的条件：
   条件成立时，要做的事情
```
注意：代码的缩进为一个Tab 键，或者4 个空格 -- 建议使用空格
- 在Python 开发中, tab 和 空格不要混用
- 注意：if 和 else语句以及各自的缩进部分共同是一个完整的代码块
##### 2、逻辑运算
- 在程序开发中，通常在判断条件时，会需要痛死判断多个条件
- 只有多个条件都满足，才能执行后续代码，这个时候需要使用逻辑运算符
- 逻辑运算符 可以把 多个条件 按照逻辑进行连接，变成 更复杂的条件
- Python 中的逻辑运算 包括：与and/ 或 or /非 not三种
###### 2.1 and
```
条件1 and 条件2
```

- 与/并且
- 两个条件同时满足，返回True
- 两个条件有一个不满足,就返回 False
###### 2.2 or
```
条件1 or 条件2
```
- 或/或者
- 两个条件只要有一个满足，返回True
- 两个条件都不满足,就返回 False

###### 2.3 not
```
not 条件1
```
- 非/不是
##### 3、elif
- 在开发中，使用if可以判断条件
- 使用else 可以处理条件不成立时的情况
- 但是如果希望在增加一些条件，条件不同，需要执行的代码也不同时，
就可以使用elif
-语法模式如下：
```
if 条件1:
   条件1满足执行的代码
elif 条件2：
   条件2满足时，执行的代码
elif 条件3：
   条件3 满足的是，执行的代码
else:
   以上条件都不满足时，执行的代码
```
- 对比逻辑运算符的代码
```
if 条件1 and 条件2:
    条件1满足 并且条件2 满足执行的代码
```
注意：
- elif 和 else 都必须和 if联合使用，而不能单独使用
- 可以将if、elif、else 以及各自缩进的代码，看诚意个完整的代码块
##### 4、if 的嵌套
- elif 的应用场景是：同时判断多个条件,所有的条件都是平级的
- 在开发中，如果使用if 进行条件判断，如果希望 在条件成立的执行语句中在添加条件判断，
就可以使用if 嵌套
- if 的嵌套的应用场景就是：在之前条件满足的前提下，在增加额外的判断
- if 的嵌套 的语法格式，除了缩进之外 和之前的没有区别
- 语法格式如下：
```
if 条件1: 

   条件1 满足执行的代码

   if 条件2:
       条件2 满足时执行的代码
   else：
       条件2 不满足时执行的代码
else: 
    条件1 不满足时，执行的代码
```
##### 随机数的处理
- 在Python 中，要使用随机数，首先要导入随机数的模块 --- "工具包"
```
import random
```
- 导入模块后，可以直接在模块名称后面敲一个. 然后按Tab键，会提示该模块中包含所有函数
- random.randint(a,b),返回 【a,b】之间的整数，包含a和b
- 列如：
```
random.randint(12,20) # 生成的随机数 12<= n <= 20
random.randint(20,20) # 结果永远是 20
random.randint(20,12) # 这句是错误的,下限必须小于上限
```
### 循环
#### 目标
- 程序的三大流程
- while 循环基本使用
- break 和 continue
- while 循环嵌套
#### 01、程序的三大流程
- 在程序开发中，一共有三种流程方式:
   - 顺序 -- 从上向下，顺序执行代码
   - 分支 -- 根据条件判断, 决定执行代码的分支
   - 循环 -- 让特定的代码 重复执行
#### 02、while 循环的基本使用
- 循环的作用就是让指定的代码重复执行
- while 循环最常用的场景就是让代码按照指定的次数重复执行
#### 2.1 while 语句的基本语法
```
出示条件设置 —— 通常是重复执行的 计数器

while 条件(判断 计数器 是否达到 目标次数)
      条件满足时,做的事情1
      条件满足时,做的事情2
      条件满足时,做的事情3
      ·····
      处理条件(计数器 + 1)
```
#### 注意: 
- while 语句以及缩进部分是一个完整的代码块
##### 死循环
由于程序员的原因，忘记在循环内部 修改循环的判断条件，导致循环持续执行，程序无法终止
#### 2.2 赋值运算符
- 在Python 中，使用 = 可以给变量赋值
- 在算术运算时, 为了简化代码的编写，Python 还提供了一系列的 与 算术运算符 对应的赋值运算符
- 注意：赋值运算符中间不能使用空格
```
 -  =   简单的赋值运算符   c=a+b 将a+b的运算结果赋值为c
   -  +=  加法的赋值运算符   c+=a 等效于 c = c + a
   -  -=  减法的赋值运算符   c-=a 等效于 c = c - a
   -  *=  乘法的赋值运算符   c*=a 等效于 c = c * a
   -  /=  除法的赋值运算符   c/=a 等效于 c = c / a
   -  //=  取整除的赋值运算符   c//=a 等效于 c = c // a
   -  %=   取模的赋值运算符   c%=a 等效于 c = c % a
   -  **=  幂赋值的赋值运算符   c**=a 等效于 c = c ** a
```
  #### 2.3 Python 中的计数方法
  1、 常见的计数方法有两种，可以分别称为：
  - 自然计数法(从1开始) -- 更符合人类习惯
  - 程序计数法(从0开始) -- 几乎所有的程序语言都选择从0开始计数
  - 因此大家在编写程序时，应尽量养成习惯：除非需求的特殊要求，否则循环的计数从0开始
  #### 2.4 循环计算
  1、在程序开发中，通常会遇到利用循环重复计算的需求
  - 遇到这种需求，可以：
  - 1、在while的上方定义一个变量，用于存放最终计算结果
  - 2、在循环体内部都用重新的计算结果，更新之前定义的变量
  #### 2.5 break 和 continue
  > break 和 continue 是专门在循环中使用的关键字
  - break **某一条件满足时**，退出循环，不在执行后续的重复代码
  - continue *某一条件满足时*, 不执行后续重复代码（直接跳到下一次循环）
  > break 和continue 只对当前所在的循环有效
  #### 知识点 (对print函数的使用做一个增强)
  - 在默认情况下，print 函数会输出内容之后，会自动在内容的末尾增加换行
  - 如果不希望末尾增加换行，可以在print 函数输出内容的后面增加 *,end=""*
  - 其中 *""* 中间可以指定print输出内容之后,继续希望显示的内容。
  - 语法格式如下:
  ```
    # 向控制台输出内容结束之后，不会换行
     print("*", end="")
    # 单纯的换行
     print("")
  ```
  > end="" 表示向控制台输出内容结束之后，不会换行   
##### 字符串的转义字符
- **\t** 在控制台输出一个制表符,协助在输出文本时 **垂直方向** 保持对齐
- **\n** 在控制台输出一个 **换行符**
> **制表符** 的功能是在不适用表格的情况下在 **垂直方向** 按列对齐文本

| 转义字符 | 描述 |
| :--- | :----: |
| *\\\\* | 反斜杠符号 |
| \\'    | 单引号    |
| \\"    | 双引号  | 
| \n    | 换行  | 
| \t    | 横向制表符  | 
| \r    | 回车  | 
### 函数基础
#### 1、函数的快速体验
##### 1.1 快速体验
- 所谓函数，就是把 **具有独立功能的代码块** 组织为一个小模块，在需要的时候 **调用**
- 哈桉树的使用包含两个步骤：     
    1.定义函数 -- **封装** 独立的功能  
    2.调用函数 -- 享受**封装**的成果
- **函数的作用**，在开发程序时，使用函数可以提高编写的效率以及代码的**重用**
#### 2、函数基本使用
##### 2.1 函数的定义
定义函数的格式如下   
 ```
    def 函数名():
        函数封装的代码
        ····
```       
1. def 是英文 define 的缩写
2. **函数名称** 应该能够表达 **函数封装代码**的功能,方便后续的调用
3. **函数名称** 的命名应该**符合 标识符的命名规则**
- 可以由 **字母、下划线**和**数字**组成
- **不能以数字开头**
- **不能以关键字重名**
##### 2.2函数调用
> 调用函数很简单的,通过函数名()即可完成对函数的调用
  - 定义好函数之后，只表示这个函数封装了一段代码而已
  - 如果不主动调用函数，函数是不会主动执行的
> 思考
 - 能否将函数放在函数定义的上方？
   - 不能！
   - 因为在使用函数名调用函数之前，必须保证python已经知道函数的存在
   - 否则控制台会提示 name 'say_hello' is not defined (名称错误：say_hello这个名字没有被定义)
##### 2.3 Pycharm 的调试工具
 - F8 Step Over 可以单步执行代码, 会把函数调用看做是一行代码直接执行
 - F7 Step Into 可以单步执行代码, 如果是函数, 会进入函数内部
 ##### 2.4 函数文档注释
 - 在开发中，如果希望给函数添加注释，应该在定义函数的下方，使用连续的**三对引号**
 - 在**连续的三对引号** 之间编写函数的说明文字
 - 在**函数调用**的位置，使用快捷键 ctrl+Q 可以查看函数的说明信息
 > *注意:* 因为 **函数体相比较独立**, 函数定义的上方, 应该和其他代码(包括注释) 保留**两个空行**
#### 3、函数的参数
#####3.1 函数参数的使用
- 在函数名的后面小括号内部填写 (参数)
- 多个参数之间使用, 分隔
```
 def sum_2_mun(num1, num2):
      result = num1, num2
      print("%d + %d = %d" %(num1, num2, result))
sum_2_num(50,20)
```
#####3.2 参数的作用
- 函数, 把既具有抵扣功能的代码块 组织为一个小模块,在需要的时候 调用
- 函数的参数，增加函数的通用性, 针对相同的数据处理逻辑，能够适应更多的数据
 1. 在函数内部，把参数当做变量使用，进行需要的数据处理
 2. 函数调用时，按照函数定义的参数顺序，把希望在函数内部处理的数据，通过参数传递
#####3.3形参和实参
- 形参：定义函数时，小括号中的参数，是用来接受参数使用的，在函数内部作为变量使用
- 实参：调用函数时，小括号中的参数，是用来把数据传递到函数内部用的
#### 4、函数的返回值
- 在程序开发中，有时候，会希望一个函数执行结束后，告诉调用者一个结果，以便调用者针对具体的结果后续处理
- 返回值 是函数完成工作后，最后给调用者的一个结果
- 在函数中使用return 关键字可以返回结果
- 在调用一方，可以使用变量来接收函数的返回结果
> 注意 return 表示返回，后续代码都不会被执行
```
def sum_2_num(num1, num2):
    """
    title:  求和函数 \n
    :param num1:  第一的传入值
    :param num2: 第二个传入值
    :return: 返回两个数的和
    """
    return num1 + num2

# 调用函数，并打印函数返回的结果
print(sum_2_num(1, 4))
```
#### 5、函数的嵌套调用
- 一个函数里面有调用了另外一个函数，这就是函数嵌套调用
- 如果函数rest2中，调用了另外一个函数test1
   - 那么执行调用rest1函数时，会先把函数test1中的任务都执行完
   - 才会回到test2中调用函数test1的位置，继续执行后续的代码
#### 6、使用模块中的函数
> 模块是Python 程序架构的一个核心概念
- 模块好比是工具包，想要使用这个工具包的工机具，就需要导入import这个模块
- 每一个以扩展名py结尾的Python源代码文件都是一个模块
- 在模块中定义的 全局变量、函数 都是模块能够提供给外即将直接使用的工具
体验小节：
- 可以在一个Python 文件中的定义变量或者函数
- 然后在另外一个文件中 使import导入这个模块
- 导入之后，就可以使用模块名.变量/模块名.函数的方式，使用这个模块中定义的变量或者函数
> 模块可以让曾经编写过的代码方便被复用！
##### 6.1 模块名也是一个标识符
 - 标识符可以由字母、下划线和数字组成
 - 不能以数字开头
 - 不能与关键字重名
 > 注意： 如果在给Python文件起名时，以数字开头是无法在Pycharm中通过导入这个模块的
##### 6.2 Pyc文件(了解)
> c 是compiled 编译过得意思   
操作步骤：
1. 浏览程序目录会发现一个_pycache_的目录
2. 目录下回有一个hm_10_分割线.cpython-35.pyc文件,cpython-35表示Python解释器版本
3. 这个pyc文件是由Python解释器将模块的源码转为字节码
- Python 这样保存字节码是作为一种启动速度的优化
**字节码**
- Python 在解释源程序时是分成两个步骤的
  1. 首先处理源代码,编译生成一个二进制字节码
  2. 再对字节码进行处理，才会生成CPU能够识别的机器码
- 有了模块的字节码文件件之后，下一次运行程序时，如果在上次保存字节码之后，没有修改过源代码，
Python 将会加载.pyc文件并跳过编译这个步骤
- 当Python 重新编译时，他会自动检查源文件和字节码文件的时间戳
- 如果你又修改了源代码，下次程序运行时，字节码将自动重新创建
> 提示：有关模块以及模块的其他导入方式，后续课程还会逐渐展开！
>模块是Python程序架构的一个核心概念
## 高级变量类型
#### 1、列表
##### 1.1 列表的定义
 - List(列表) 是Python 中使用最频繁的数据类型，在其他语言中通常叫做数组
 - 专门用于存储一串信息
 - 列表用[] 定义, 数据局之间使用，分隔
 - 列表索引从0 开始
    - 索引就是数据在列表中的位置编号，索引又可以被称为下标
> 注意：从列表中取值时，如果超出索引范围，程序会报错
```
  name_list =["zhangsan", "lisi", "wangwu"]
```
##### 1.2 列表常用操作
- 在ipython3中定义一个列表，列如： name_list=[]
- 输入name_list.按下Tab键，ipython 会提示列表能够欧使用的方法如下：
```
  name_list.append  name_list.count  name_list.insert  name_list.reverse
  name_list.clear   name_list.extend name_list.pop     name_list.sort
  name_list.copy    name_list.index  name_list.remove  
```
| 序号 | 分类 | 关键字/ 函数/ 方法| 说明| 
| :--- | :----: |:----: |:----: |
| 1 | 增加 |列表.insert(索引，数据) |在指定位置插入数据
|  |  |列表.append(数据) |在末尾追加数据
|  |  |列表.extend(列表2) |将列表2的数据追加到列表
| 2 | 修改 |列表[索引] = 数据 |修改指定索引的数据
| 3 | 删除 |del 列表[索引] |删除指定索引的数据
|  |  |列表.remove[数据] |删除第一个出现的指定数据
|  |  |列表.pop[数据] |删除末尾数据
|  |  |列表.pop(索引) |删除指定索引数据
|  |  |列表.clear |清空列表
| 4 | 统计 |len(列表) |列表长度
|  | |列表.count(数据) |数据在列表中出现的次数
| 5 | 排序|列表.sort() |升序排序
|  | |列表.sort(reverse=True) |降序排序
|  | |列表.reverse() |逆序、反转

- 使用del 关键字(delete) 同样可以删除列表中元素
- del 关键字本质上是用来 将一个变量从内存中删除的
- 如果使用 del 关键字将变量从内存中删除，后续的代码就不能再使用这个变量了
```
 del name_list[2]
```
> 在日常开发中，要从列表删除数据，建议使用列表提供的方法

关键字、函数和方法(科普)
- 关键字 是Python内置的、具有特殊意义的标识符
> 关键字后面不需要使用括号
- 函数 封装了独立功能、可以直接调用
```
函数名(参数)
```
> 函数需要四甲基硬背
- 方法和和函数类似、同样是封装了独立功能
- 方法需要通过对象来调用，表示针对这个对象要做的做操作
```
 对象.方法名
```
> 在变量后面输入. ,然后选择针对这个变量要执行的操作，记忆起来比函数简单的多
##### 1.3 循环遍历
- 遍历 就是 从头到尾依次从列表中获取数据
   - 在循环体内部 针对 每一个元素, 执行相同的操作
- 在Python 中为了 提高列表的遍历效率, 专门提供的迭代iteration遍历
- 使用for就能够实现迭代遍历
```
   # for 循环内部使用的变量 in 列表
       for name in name_list:
             循环内部针对列表元素进行操作
              print(name)
```
应用场景
 - 尽管Python 的列表中可以存储不同类型的数据
 - 但是在开发中, 更多的应用场景是
    1. 列表存储相同类型的数据
    2. 通过迭代遍历,在循环体内部，针对列表中的每一项元素，执行相同的操作
#### 2、元组
#####2.1元组的定义
 - Tuple(元组) 与列表类似，不同之处在于元组的元素不能修改
    - 元组 表示多个元组组成的序列
    - 元组 在Python 开发中，有特定的应用场景
- 用于存储一串信息，数据之间使用, 分隔
- 元组用()定义
- 元组的索引从0开始
   - 索引就是数据在元组中位置编号
```
into_tuple = ("zhangsan", 18, 1.75)
```
创建空元组
```
 tuple = ()
```
元组中 只包含一个元素时，需要在元素后面添加逗号
``` 
single_tuple = (2,)
```
##### 2.2 元组常用操作
- 在python3中 定义一个元组,列如： info=()
- 输入info. 按下Tab 键，python 会提示元组能够使用的函数如下：
```
  info.index   info.count
```
##### 2.3 循环遍历
 - 取值就是从元组中获取存储在指定位置的数据
 - 遍历就是从头到尾依次从元组中获取数据
```
  # for 循环内部使用的变量 in 元组
    for  item in info:
      循环内部针对元组元素进行操作
      print(item)
```
> - 在Python 中，可以使用for循环遍历所有非数字型类型的变量: 列表、元组、字典、以及字符串
> - 提示： 在实际开发中，除非能够确认元组中的数据类型，否则针对元组的循环遍历需求并不是很多
##### 2.4应用场景
- 尽管可以使用for in遍历元组
- 但是在开发中，更多的应用场景是：
   - 函数的参数和返回值，一个函数可以接受任意多个参数，或者一次返回多个数据
      - 有关函数的参数 和返回值，在后续函数高级给大家介绍
   - 格式化字符串，格式化字符串后面的() 本质就是一个元组
   - 让列表不可以被修改，以保护数据安全
```
   info_tuple = ("zhangsan", 18)
   print("%s 的年龄是 %d" % info)
```

元组和列表之间的转换
- 使用list函数可以把元组转换成列表
```
 list(元组)
```
- 使用tuple函数可以把列表转换成元组
```
  tuple(列表)
```
#### 3、字典
##### 3.1 字典的定义
- `dictionary`(字典) 是除了列表以外的 Python 之中最灵活的数据类型
- 字典同样可以用来存储多个数据
   - 通常用于存储描述一个 物体的相关信息
- 和列表的区别
   - 列表是有序的对象集合
   - 字典是无序的对象集合
- 字典用{}定义
- 字典使用键值对存储数据,键值对之间使用`,`分隔
   - 键 key 是索引
   - 值 value 是数据
   - 键和值之间使用`:`分隔
   - 键必须是唯一的
   - 值可以取任何数据类型，但 键只能使用字符串、数字或元组
```
  xiaoming = {
      "name": "小明",  
      "age": 18,  
      "gender": True,  
      "height": 1.75,  
}
```
##### 3.2字典常用操作
- 在ipython3中定义一个字典，列如: xm_dict = {}
- 输入xm_dict. 按下Tab 键，ipython会提示字典能够使用的函数如下：
```
xm_dict.clear       xm_dic.items        xm_dict.setdefault
xm_dict.copy        xm_dict.keys        xm_dict.update
xm_dict.fromkeys    xm_dict.pop         xm_dict.values
xm_dict.get         xm_dict.popitem
```
##### 3.3循环遍历
- 遍历就是依次从字典中获取所有键值对
```
 # for 循环内部使用的 `key 的变量` in 字典
    for k in xiaoming:
         print("%s: %s" %(k,  xiaoming[key]))
```
> 提示：在实际开发中，由于字典中每一个键值对保存的数据类型是不同的，所以针对字典的循环遍历需求并不是很多
##### 3.4 应用场景
- 尽管可以使用`for in`遍历字典
- 但是在开发中，更多的应用场景是:
   - 使用多个键值对，对存储描述一个 `物体` 的相关信息 -- 描述更复杂的数据信息
   - 将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
```
   card_list = [{"name": "张三",
                "qq": "123456",
                "phone": "110"
                },{"name": "张三",
                "qq": "123456",
                "phone": "110"
                }]
```
#### 4字符串
##### 4.1字符串的定义
- 字符串就是一串字符，是编程语言中便是文本的数据类型
- 在Python中可以使用一对双引号`"` 或者 一对单引号`'`定义一个字符串
    - 虽然可以使用`\"` 或者`\'`做字符的转义，但是在实际开发中:
        - 如果字符串内部需要使用`"`,可以使用`'`定义字符串
        - 如果字符串内部需要使用`'`,可以使用`"`定义字符串
- 可以使用索引获取一个字符串中指定位置的字符，索引计数从0开始
- 也可以使用`for`循环遍历字符串中每一个字符
> 大多数编程语言都是用`"`来定义字符串
```
string = "hello Python"
for c in string:
    print(c)
```
##### 4.2字符串的常用操作
- 在ipython3中定义一个字符串, 例如：hello_str = ""
- 输入hello_str. 按下TAB键, ipython 会提示字符串能够使用的方法如下：
```
hello_str.captailize        hello_str.isidentifier      hello_str.rindex
hello_str.casefold          hello_str.islower           hello_str.rjust
hello_str.center            hello_str.isnumberic        hello_str.rpartition
hello_str.count             hello_str.isprintable       hello_str.rsplit
hello_str.encode            hello_str.isspace           hello_str.rstrip
hello_str.endswith          hello_str.istitle           hello_str.split
hello_str.expandtabs        hello_str.isupper           hello_str.splitlines
hello_str.find              hello_str.join              hello_str.startswith
hello_str.format            hello_str.ljust             hello_str.strip
hello_str.format_map        hello_str.lower             hello_str.swapcase
hello_str.index             hello_str.lstrip            hello_str.title
hello_str.isalnum           hello_str.maketrans         hello_str.translate
hello_str.isalpha           hello_str.partition         hello_str.upper
hello_str.isdecimal         hello_str.replace           hello_str.zfill
hello_str.isdigit           hello_str.rfind
```
>提示：正是因为python内置提供的方法足够多，才使得在开发时，能够针对字符串进行更加灵活的操作！应对更对的开发需求！

1）判断类型

| 方法 | 说明 | 
| :--- | :----: |
| string.isspace() | 如果string中只包含空格,则返回True |
| string.isalnum() | 如果string中至少有一个字符并且所有的字符都是字母或者数字则返回True |
| string.isalpha() | 如果string中至少有一个字符并且所有字符都是字母则返回True |
| string.isdecimal() | 如果string只包含数字则返回True,全角数字 |
| string.isdigit() | 如果string只包含数字则返回True,全角数字、(1)、\u00b2 |
| string.isnumeric() | 如果string只包含数字则返回True,全角数字、汉字数字|
| string.istitle() | 如果string是标题化的(每个单词的首字母大写)则返回True|
| string.islower() | 如果string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写,则返回True|
| string.isupper() | 如果string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写,则返回True|

2）查找和替换

| 方法 | 说明 | 
| :--- | :----: |
| string.startswith(str) | 检查字符串是否以Str开头,是则返回True |
| string.endswith(str) | 检查字符串是否以Str结束,是则返回True |
| string.find(str,start=0,end=len(string)) | 检查str是否包含在String中,如果start和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引，否则返回-1 |
| string.rfind(str,start=0,end=len(string)) | 类似于find()函数，不过是从右边开始查找 |
| string.index(str,start=0,end=len(string)) | 跟find()方法类似，只不过如果str不在string 中会报错|
| string.rindex(str,start=0,end=len(string)) | 类似于index()函数，不过是从右边开始查找|
| string.replace(old_str,new_str,nun=string.count(old)) | 把string中的old_str 替换成 new_str,如果num指定，则替换不超过num次|

3）大小写转换

| 方法 | 说明 | 
| :--- | :----: |
| string.capitalize(str) | 把字符串的第一个字符大写 |
| string.title(str) | 把字符串的每个单词首字母大写 |
| string.lower(str) | 转换string中所有大写字符为小写 |
| string.upper(str) | 转换string中所有小写字符为大写 |
| string.swapcase(str) | 翻转string中的大小写 |

4）文本对齐

| 方法 | 说明 | 
| :--- | :----: |
| string.ljust(width) | 返回一个原字符串左对齐，并使用空格填充至长度width的新字符串 |
| string.rjust(width) | 返回一个原字符串右对齐，并使用空格填充至长度width的新字符串 |
| string.center(width) | 返回一个原字符串居中对齐，并使用空格填充至长度width的新字符串 |

5）去除空白字符

| 方法 | 说明 | 
| :--- | :----: |
| string.lstrip(str) | 截取string左边(开始)的空白字符 |
| string.rstrip(str) | 截取string右边(末尾)的空白字符 |
| string.strip(str) | 截取string左右两边的空白字符 |

6）拆分和连接

| 方法 | 说明 | 
| :--- | :----: |
| string.partition(str) | 把字符串string分成一个3元素的元组(str前面,str,str后面)|
| string.rpartition(str) | 类似于partition()函数,不过是从右边快开始查找|
| string.split(str="",num) | 以str为分隔符切片string,如果num有指定值,则仅分隔num+1个子字符串,str默认包含'\t','\r','\n'和空格|
| string.splitlines() | 按照行('\r','\n','\r\n')分隔,返回一个包含各行作为元素的列表|
| string.join(seq) | 以string作为分隔符,将seq中所有的元素(的字符串表示)合并为一个新的字符串|
##### 4.3 字符串的切片
- 切片 方法适用于字符串、列表、元组
   - 切片使用索引值来限定范围，从一个大的字符串中切出小的字符串
   - 列表 和元组都是有序的集合，都能够 通过索引值获取到对应的数据
   - 字典是一个无序的集合，是使用键值对保存数据

```
字符串[开始索引:结束索引:步长]
```
注意：   
1. 指定的区间属于左闭右开型 `[开始索引, 结束索引]` => `开始索引 >= 范围 < 结束索引`         
   - 从`起始`位开始，到`结束`的前一位 结束(不包含结束位本身) 
2. 从头开始, 开始索引 数字可以省略，冒号不能省略
3. 到末尾结束, 结束索引数字可以省略, 冒号不能省略
4. 步长默认为`1`, 如果连续切片, 数字和冒号都可以省略
```
字符串的截取,负数值从末尾往前移动.
列如： num_str ="0123456789"
      num_str[2:-1] 
输出的结果：'2345678'
```

#### 5、公共方法
##### 5.1 Python 内置函数
python 包含了以下内置函数:

| 方法 | 描述 |  备注 | 
| :--- | :----: | :----: |
| len(item) | 计算容器中元素个数 |  |
| del(item) | 删除变量 | del有两种方式 |
| max(item) | 返回容器中元素最大值 | 如果是字典, 只针对key比较 |
| min(item) | 返回容器中元素最小值 | 如果是字典, 只针对key比较 |
| cmp(item1,item2) | 比较两个值, -1小于/0 相等/1 大于 | python3.x取消了cmp函数 |
注意：
 - 字符串 比较符合以下规则: "0" < "A" < "a"
 ##### 5.2 切片
 
| 描述 | Python |  结果 |  支持的数据类型| 
| :--- | :----: | :----: |  :----:|
| 切片 | "0123456789"[::-2] | "97531"  |字符串、列表、元组 |
- 切片使用索引值来限定范围, 从一个大的字符串中切出小的字符串
- 列表和元组都是有序的集合, 都能够通过索引值获取到对应的数据
- 字典是一个无序的集合, 是使用键值对保存数据
```
  注意： 字典和字典之间不能比较大小
```
#####　5.3 运算符

| 运算符 | Python表达式 |  结果 |  描述| 支持的数据类型|
| :--- | :----: | :----: |  :----:| :----:|
| + | [1,2]+[3,4] | [1,2,3,4]  | 合并 | 字符串、列表、元组|
| * | ["Hi!"] * 4 | ["Hi!","Hi!","Hi!","Hi!"]  | 重复 | 字符串、列表、元组|
| in | 3 in (1,2,3) | True  | 元素是否存在 | 字符串、列表、元组、字典|
| not in | 4 not  in (1,2,3) | True  | 元素是否不存在 | 字符串、列表、元组、字典|
| > >= == < <=  | (1,2,3)  < (2,2,3) | True  | 元素比较 | 字符串、列表、元组|

注意：
 - `in` 在对字典操作时, 判断的时字典的键
 - `in` 和 `not in` 被称为 成员运算符   

成员运算符    
成员运算符用于测试序列中是否包含指定的成员

| 运算符 | 描述 |  实例 | 
| :---: | :----: | :----: | 
| in | 如果在指定的序列中找到值返回True, 否则返回False| 3 in (1, 2, 3)返回True | 
| not in | 如果在指定的序列中找到值返回True, 否则返回False| 3 not in (1, 2, 3)返回False | 
注意：在对字典操作时，判断的是字典的键

##### 5.4 完整的for循环语法
- 在`Python`中完整的`for循环`的语法如下：
```
   for 变量 in 集合: 
        循环代码
   else: 
       没有通过 break 退出循环，循环结束后，会执行的代码
```
应用场景
 - 在迭代遍历嵌套的数据类型时, 列如一个列表包含了多个字典
 - 需求：要判断 某一个字典中，是否存在指定的值
     - 如果存在， 提示并且退出循环
     - 如果不存在，在循环体整体结束后, 希望得到一个统一的提示
```
student = [
    {"name": "阿土"},
    {"name": "小美"}
]

# 在学员列表中搜索指定的姓名
find_name = "阿土"

for stu_dict in student:

    print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到了：%s" % find_name)
        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望得到一个统一的提示
    print("抱歉 没有找到 %s" % find_name)

print("循环结束")
```
#### Linux 上的Shebang符号(#!)
- ***#!*** 这个符号叫Shebang 或者 She-bang
- Shebang 通常在Unix 系统脚本中的**第一行开头**使用
- 指明**执行这个脚本文件**算**解释程序**

##### 使用Shebang 的步骤
1、使用 which 查询 python3的解释器所在路径
```
 which python3
```
2、修改运行的主 python文件，在第一行增加以下内容
```
#! /usr/bin/python3(解释器地址)
```
3、修改主python 文件的权限，增加执行权限
```
chmod +x cards_main.py
```
4、在需要时执行程序即可
```
./card_main.py
```
#### 6变量进阶
##### 6.1 变量的引用
> 1、变量 和 数据 都是保存在内存中的    
> 2、在python中的函数的参数传递以及返回值

###### 6.1.1 引用的概念
在python中
- **变量**和 数据是分开存储的
- **数据**保存在内存中的一个位置
- **变量**中保存着数据在内存中的地址
- **变量**中**记录数据的地址**，叫做引用
- 使用 id() 函数可以查看变量中保存数据所在的内存地址

> 注意：如果变量已经被定义，当给一个变量赋值的时候，本质上是修改了数据的引用   
>  1、**变量不在**对之前的数据引用   
>  2、**变量改为**对新的赋值的**数据引用** 

##### 6.2 可变和不可变
- **不可变类型**, 内存中的数据不允许被修改
    - 数字类型 int, bool, float, complex,long(2.x)
    - 字符串 str
    - 元组 tuple
- **可变类型**, 内存中的数据可以被修改：
    - 列表 list
    - 字典 dict

> 注意：字典的key 只能使用不可以变类型的数据

**注意**：
1、可变类型的数据变化,是通过方法来实现的
2、如果给一个可变类型的变量，赋值一个新的数据，引用会修改
- 变量不在对之前的数据引用
- 变量改为对赋值的数据引用

**哈希(hash)**
- python 中内置有一个名字叫做hash(o)的函数
  - 接受一个**不可变类型**的数据作为**参数**
  - 返回结果是一个**整数**
- 哈希是一种算法，其作用就是提取数据的**特征码**(指纹)
  - 相同的内容 得到 相同的结果
  - 不同的内容 得到 不同的结果
- 在Python中, 设置字典的键值对时，会首先对key进行hash 已决定如何在内存中保存字典的数据，
以便后续对字典的操作: 增、删、改、查
  - 键值对的 key 必须是不可变类型的数据
  - 键值对的value 可以是任意类型的数据

##### 6.3 局部变量和全局变量
- 局部变量是正在函数内部定义的变量，只能在函数内部使用
- 全局变量是在函数外部定义的变量 (没有定义在某一个函数内)，所有函数内部都可以使用这个变量
> 提示：在其他的开发语言中，大多 不推荐使用全局变量 --可变范围太大 导致程序不好维护

###### 6.3.1 局部变量
- 局部变量是在函数内部定义的变量
- 函数执行结束后，函数内部的局部变量，会被系统回收
- 不同的函数，可以定义相同的名字的局部变量，但是各用个的都不会产生影响

局部变量的作用
- 在函数内部使用，临时保存函数内部需要使用的数据

局部变量的生命周期
- 所谓的 生命周期 就是变量从被创建到被系统回收的过程
- 局部变量在函数执行时才会被创建
- 函数执行结束后 局部变量 被系统回收
- 局部变量在生命周期内，可以用来存储函数内部临时使用到的数据

###### 6.3.2 全局变量
- 全局变量就是函数外部定义的变量，所有的函数内部都可以使用这个变量

注意：函数执行时，需要处理变量时 会：
1、首先 查找 函数内部 是否存在 指定名称的局部变量，如果有，直接用
2、如果没有，查找函数外部是否存在指定名称的全局变量，如果有，直接用
3、如果还没有 程序报错

1) 函数不能之际修改 全局变量的引用
- 全局变量是在 函数外部定义的 变量 (没有 定义在某一个函数内)，所有函数内部都可以使用这个变量
> 提示：在其他的开发语言中，大多 不推荐使用全局变量 --可变范围太大 导致程序不好维护！

- 在函数内部，可以通过全局变量的引用获取对应的数据
- 但是， 不允许直接修改全局变量的引用 -- 使用赋值语句修改全局变量的值

2) 在函数内部修改全局变量的值
- 如果函数内部需要修改全局变量，需要使用global进行声明

3) 全局变量定义的位置
- 为了保证所有的函数都能够正确使用到全局变量，应该将全局变量定义在其他函数的上方。


代码结构示意图如下   

| 顺序 |
| :--- | 
|shebang| 
|import模块|
|全局变量|
|执行代码|

4) 全局变量命名的建议
- 为了避免局部变量和全局变量出现混淆 在定义全局变量时
- 全局变量名应该增加 g_ 或者 gl_ 的前缀
> 提示：具体的要求格式，各公司要求可能会有些差异


5) is 和  === 区别
- is 是用来判断 两个变量引用的对象是否为同一个
- === 用于判断引用的变量的值是否相等

### 7继承

面向对象的三大特性
1、封装 根据 职责将属性和方法封装到一个抽象的类中
2、继承 实现代码的重用，相同的代码不需要重复编写
3、多态 不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度

##### 7.1 单继承
####### 7.1.1 继承的概念、语法和特点
继承的概念：子类 拥有和父类的所有方法和属性
