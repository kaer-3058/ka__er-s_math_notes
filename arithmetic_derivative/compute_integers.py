""" 计算非负整数 n 的算数导数 D(n) """

def arithmetic_derivative(n: int) -> int:
    # 处理 0 和 1 的边界情况
    if n in (0, 1):
        return 0

    temp = n
    total_sum = 0.0
    d = 2

    # 质因数分解并累加 e_i / p_i
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            total_sum += count / d
        d += 1

    # 处理剩余的大质因数
    if temp > 1:
        total_sum += 1 / temp

    # D(n) = n * sum(e_i / p_i)
    return round(n * total_sum)

#在这里输入
num = 6
print(f"D({num}) = {arithmetic_derivative(num)}")
