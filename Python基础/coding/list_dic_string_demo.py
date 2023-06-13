# 字符串是不可变的，可以整个重新赋值，不可以更改其中的字符
name = 'hahahaha you are so funny!'
# print(name[9:12] + ' are so cute')

name = 'you'
# print(name)

# name[0] = 'i' 
# 报错 TypeError: 'str' object does not support item assignment


# 列表是可变的
name = ['you', 'are', 'so', 'funny']
# for x in name:
#     print(x, end=' ')
# print('\n')

# 列表可以修改其中的item
# name[3] = 'cute'
# for x in name:
#     print(x, end=' ')

# 列表的remove()和append()方法
# name.append('!')
# for x in name:
#     print(x, end=' ')
# name.remove('!')
# for x in name:
#     print(x, end=' ')

# 元组 输入时用() ；列表用[]
# 元组是不可变数据类型
lsp = ('hello', 'lsp')
# print(lsp[0], lsp[1])
# print(lsp[0:1])   # ('hello',)

# print(len(lsp))   # 2

# tuple() 将列表转换为元组
tp = tuple(['you', 'are', 'so', 'funny'])
# print(tp)
# list() 将元组转换为列表
list = list(('hello', 'lsp'))
# print(list)


# 字典不排序，可以使用任意值作为key值
sb = {'name':'cccc', 'age':'22', 'gender':'female'}

# for x in sb:
#     print(x + ' : ' + sb[x])

# keys()、values() 、items()
# print('---------key-------')
# for x in sb.keys():
#     print(x)

# print('---------values-------')
# for x in sb.values():
#     print(x)

# print('---------items-------')
# for x in sb.items():
#     print(x)


# 字典数据类型 get() 方法

# print(sb.get('name','null'))
# 如果字典里面没有该key值，则直接返回备用值
# print(sb.get('lover','null'))

# 字典中的 setdefault（）方法：当没有该key值时，新建并赋值，有该key值时返回value值
# print(sb.setdefault('color', 'black'))
# print(sb)
# print(sb.setdefault('color', 'red')) # 第一步已经为color设置默认值，现在直接返回value值

