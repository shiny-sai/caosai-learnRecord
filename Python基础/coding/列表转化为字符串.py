# 编写一个函数，它以一个列表值作为参数，返回一个字符串。
# spam = ['apples', 'bananas', 'tofu', 'cats']
# 该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。
# 例如，将前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
# 但你的函数应该能够处理传递给它的任何列表。

# Author: caosai
# Date: 2022/11/22

def trans_to_str(spam):
    _str = ''
    if(len(list) == 1):
        _str = spam[-1]
    else:
        for i in range(len(spam)-1):
            _str = _str + spam[i] + ', '
        _str = _str + 'and ' + spam[-1]
    print(_str)
    return _str

while(1):
    print('请输入列表的各项(以空格结束):')
    str1 = input()
    list = str1.split()
    if(len(list) != 0):
        trans_to_str(list)
