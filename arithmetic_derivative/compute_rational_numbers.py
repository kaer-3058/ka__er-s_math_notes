from fractions import Fraction

def integer_arithmetic_derivative(n: int) -> int:
    """计算整数 n 的算术导数 D(n)"""
    if n == 0 or n == 1 or n == -1:
        return 0
    if n < 0:
        return -integer_arithmetic_derivative(-n)

    temp = n
    total_sum = Fraction(0, 1)
    d = 2

    # 质因数分解：D(n) = n * sum(e_i / p_i)
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            total_sum += Fraction(count, d)
        d += 1

    if temp > 1:
        total_sum += Fraction(1, temp)

    return int(n * total_sum)

def rational_arithmetic_derivative(q: Fraction | int) -> Fraction:
    """计算有理数 q 的算术导数 D(q)"""
    q = Fraction(q)
    a, b = q.numerator, q.denominator

    # 商法则：D(a/b) = (D(a)*b - a*D(b)) / b^2
    da = integer_arithmetic_derivative(a)
    db = integer_arithmetic_derivative(b)

    return Fraction(da * b - a * db, b**2)


#在这里输入
q = Fraction(3, 4)  #有理数 3/4
print(f"D({q}) = {rational_arithmetic_derivative(q)}")
