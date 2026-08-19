from fractions import Fraction
import math
import os
import matplotlib.pyplot as plt

# 算术导数核心算法
def integer_arithmetic_derivative(n: int) -> int:
    """计算整数 n 的算术导数 D(n)"""
    if n in (0, 1, -1): return 0
    if n < 0: return -integer_arithmetic_derivative(-n)

    temp, total_sum, d = n, Fraction(0, 1), 2
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

def rational_arithmetic_derivative(q: Fraction) -> Fraction:
    """计算有理数 q 的算术导数 D(q)"""
    a, b = q.numerator, q.denominator
    da = integer_arithmetic_derivative(a)
    db = integer_arithmetic_derivative(b)
    return Fraction(da * b - a * db, b**2)

# 发散采样生成器
def generate_hyper_unbounded_samples(max_points):
    """生成采样点"""
    points = set()

    def is_prime(num):
        if num < 2: return False
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0: return False
        return True

    # A. 基础骨架：Farey 序列保证 [0, 1] 基础覆盖
    N = 80
    a, b, c, d = 0, 1, 1, N
    points.add(Fraction(a, b))
    while c <= N and len(points) < 3000:
        points.add(Fraction(c, d))
        k = (N + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b

    # B. 2^m 与质数 p 结合
    primes = [p for p in range(3, 1000) if is_prime(p)]
    for m in range(10, 35):
        pow2 = 2**m
        for p in primes:
            if len(points) >= max_points * 0.7: break
            rem = pow2 % p
            if rem != 0:
                points.add(Fraction(rem, p))

    # C. 阶乘 k! 与质数结合
    for k in range(5, 12):
        fact = math.factorial(k)
        for p in primes[:50]:
            if len(points) >= max_points: break
            rem = fact % p
            if rem != 0:
                points.add(Fraction(rem, p))

    # D. 补齐剩余质数点
    p = 2
    while len(points) < max_points:
        if is_prime(p):
            points.add(Fraction(1, p))
            points.add(Fraction(p - 1, p))
        p += 1

    return sorted(list(points))

# 主程序：计算、文件输出与实时绘图
if __name__ == "__main__":
    # 指定输出文件路径
    output_path = r"output.txt"

    # 若文件夹不存在，自动创建
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("1. 正在生成发散采样点...")
    samples = generate_hyper_unbounded_samples(max_points = 500000)

    x_vals = []
    y_vals = []

    print("2. 正在计算算术导数并同步写入文件...")
    with open(output_path, "w", encoding="utf-8") as f:
        for q in samples:
            dq = rational_arithmetic_derivative(q)
            
            # 写入文本文件（保持分式精确格式）
            print(f"({q},{dq}),", file=f)
            
            # 同时收集用于绘图的浮点数坐标
            x_vals.append(float(q))
            y_vals.append(float(dq))

    print(f"数据成功保存至：\n{os.path.abspath(output_path)}")

    # 3. 实时绘制图像
    print("3. 正在生成折线/散点图...")
    plt.figure(figsize=(12, 7))
    plt.scatter(x_vals, y_vals, s=3, color="crimson", alpha=0.6)

    plt.xlim(0, 1)
    plt.title("Extreme Unbounded Arithmetic Derivative D(q) in [0, 1]", fontsize=13)
    plt.xlabel("q")
    plt.ylabel("D(q)")
    plt.grid(True, which="both", linestyle=":", alpha=0.5)

    print(f"最大极值: {max(y_vals):.2e}")
    print(f"最小极值: {min(y_vals):.2e}")
    
    plt.show()
