''' 代码语言：Python '''

import math
from scipy.special import lambertw

def theta(t): #相位函数 theta(t)
    return (t / 2.0) * (math.log(t / (2.0 * math.pi)) - 1.0) - math.pi / 8.0

def M_val(t): #M 参数
    return math.floor(math.sqrt(t / (2.0 * math.pi)))

def p_val(t): #p 参数
    return math.sqrt(t / (2.0 * math.pi)) - M_val(t)

def C0(t): #C0 参数
    p = p_val(t)
    return math.cos(2.0 * math.pi * (p**2 - p - 1.0/16.0)) / math.cos(2.0 * math.pi * p)

def C1(t): #C1 参数
    p = p_val(t)
    return 1.84 * (p - 0.5)**5 - 0.0485 * (p - 0.5)

def C2(t): #C2 参数
    p = p_val(t)
    return 0.95 * abs(p - 0.5)**7 - 0.183 * (p - 0.5)**4 + 0.0052

def R(t): #余项 R
    M = M_val(t)
    tt = t / (2.0 * math.pi)
    return ((-1)**(M - 1)) * (tt**(-0.25)) * (C0(t) + C1(t) * (tt**(-0.5)) + C2(t) * (tt**(-1.0)))

def Z(t): #主函数 Z(t)
    M = M_val(t)
    sum_term = 0.0
    th = theta(t)
    for n in range(1, M + 1):
        sum_term += math.cos(th - t * math.log(n)) / math.sqrt(n)
    return R(t) + 2.0 * sum_term

def g(n): #第 n 个非平凡零点的虚部估计函数
    x = n - 7.0/8.0
    # scipy 的 lambertw 返回的是复数对象，这里只需要它的实部 (.real)
    w_val = lambertw(x / math.e).real
    return (2.0 * math.pi * x) / w_val

def find_zeta_zero(n, max_iter=5): #割线法
    t0 = g(n)
    t_prev = t0 - (2.0 * math.pi) / math.log(t0)
    z0 = Z(t0)
    z_prev = Z(t_prev)
    print(f"计算第 {n} 个非平凡零点:")
    print(f"初始值: t_0 = {t0:.3f}, t_{{-1}} = {t_prev:.3f}")
    
    # 迭代
    for i in range(1, max_iter+1):
        # 避免分母为0
        if z0 - z_prev == 0:
            print("警告: 遇到极值或迭代精度达到极限，停止迭代")
            break
        t_next = t0 - z0 * (t0 - t_prev) / (z0 - z_prev)
        t_prev = t0
        z_prev = z0
        t0 = t_next
        z0 = Z(t0)
        
        # 使用 :.10f 控制打印 10 位小数
        print(f"第 {i} 次迭代: {t0:.10f}")

    print(f"\n--> 最终计算得到的零点约等于: 0.5 + {t0:.10f} i\n")
    return t0

# 计算第n个非平凡零点
n = 5
if __name__ == "__main__":
    find_zeta_zero(n)
