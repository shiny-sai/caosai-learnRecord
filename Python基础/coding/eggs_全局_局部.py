def spam():
    eggs = 'bad eggs'
    print(eggs) # 输出 bad eggs

def bacon():
    eggs = 'good eggs'
    print(eggs) # 输出 good eggs
    spam()      # 输出 bad eggs
    print(eggs) # 输出 good eggs

eggs = 'global eggs'
bacon()
print(eggs)


# 预计输出 good eggs / bad eggs / good eggs / global eggs
