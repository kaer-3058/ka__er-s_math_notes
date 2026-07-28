'''
使用梅钦公式计算圆周率
'''

def machin_pi(n):
    t = n + 10  #多计算10位，防止尾数取舍的影响
    b = 10 ** t
    x1 = b * 4 // 5
    x2 = b // -239
    s = x1 + x2
    n *= 2
    for i in range(3, n, 2):
        x1 //= -25
        x2 //= -57121
        x = (x1 + x2) // i
        s += x
    pi = s * 4
    pi //= 10 ** 11  #舍掉后十位
    s = str(pi)
    return s[0] + "." + s[1:]

# 执行计算，n是位数
n = 50
pi = machin_pi(n)
print(f"梅钦公式计算结果: {pi}")
