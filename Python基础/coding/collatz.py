# collatz()函数

# Author: caosai

# Date: 2022/11/13

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    return number

while(1):
    print("请输入一个正整数：")
    try:
        number = int(input())
    except(ValueError):
        print("输入数据无效！请输入一个正整数！")
    print(number)
    while(number != 1):
        number = collatz(number)
        print(number)
