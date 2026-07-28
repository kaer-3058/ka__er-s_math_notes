'''
使用拉马努金公式计算圆周率
公式: 1/π = (2√2)/9801 * Σ [ (4n)! / (n!)^4 ] * [ (1103 + 26390n) / (396)^(4n) ]
每一项约增加8位有效数字
'''

import math
from decimal import Decimal, getcontext

def ramanujan_pi(precision):
    getcontext().prec = precision + 5  # 多算几位避免舍入误差
    
    coefficient = (Decimal(2) * Decimal(2).sqrt()) / Decimal(9801)
    total = Decimal(0)
    n = 0

    while True:
        # 计算各项
        numerator = math.factorial(4 * n) * (1103 + 26390 * n)
        denominator = (math.factorial(n) ** 4) * (396 ** (4 * n))
        term = Decimal(numerator) / Decimal(denominator)
        total += term
        
        # 当项小于精度阈值时停止
        if term < Decimal(10) ** ( -(precision + 2)):
            break
        n += 1
    
    pi = Decimal(1) / (coefficient * total)
    return pi.quantize(Decimal('0.' + '0' * (precision - 1)))

# 执行计算，precision是位数
precision = 50
pi = ramanujan_pi(precision)
print(f"拉马努金公式计算结果: {pi}")
