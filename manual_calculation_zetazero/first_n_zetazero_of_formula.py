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

def find_zeta_zero(n, max_iter=5): # 割线法
    t0 = g(n)
    t_prev = t0 - (2.0 * math.pi) / math.log(t0)
    
    # 迭代
    for i in range(1, max_iter+1):
        # --- 保护层：确保输入合法 ---
        if t0 <= 0 or t_prev <= 0:
            # 如果出现负数，说明迭代已经逃逸，返回一个标记值或跳出
            return float('nan') # 或者你可以返回 t0 的旧值
        
        z0 = Z(t0)
        z_prev = Z(t_prev)
        
        if z0 - z_prev == 0:
            break
            
        t_next = t0 - z0 * (t0 - t_prev) / (z0 - z_prev)
        t_prev = t0
        t0 = t_next
        
    return t0

# 计算第n个非平凡零点
# n = 1
# if __name__ == "__main__":
#     find_zeta_zero(n)


from mpmath import mp, zetazero

# 设置计算精度（例如50位十进制精度）[citation:3]
# mp.dps = 50

# 计算第 n 个非平凡零点
# n = 1
# zero = zetazero(n)


import os
import pandas as pd
import time

def test_total_time_performance(n_count, save_dir):
    """
    n_count: 要计算的零点总个数 (例如 1000)
    save_dir: 保存路径
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    file_path = os.path.join(save_dir, "总耗时测试报告.xlsx")
    
    print(f"正在计算前 {n_count} 个零点，请稍候...")
    
    # 记录总开始时间
    total_start_time = time.perf_counter()
    
    # 执行循环计算
    for j in range(1, n_count + 1):
        find_zeta_zero(j)
        
    # 记录总结束时间
    total_end_time = time.perf_counter()
    total_elapsed_time = total_end_time - total_start_time
    
    print("-" * 30)
    print(f"计算完成！")
    print(f"总计算个数: {n_count}")
    print(f"总耗时: {total_elapsed_time:.6f} 秒")
    
    # 存入数据到 Excel
    results = [{
        "测试对象": f"前 {n_count} 个零点",
        "计算总个数": n_count,
        "总耗时(秒)": total_elapsed_time,
        "平均每个零点耗时(秒)": total_elapsed_time / n_count
    }]
    
    df = pd.DataFrame(results)
    df.to_excel(file_path, index=False)
    print(f"数据已保存至：{file_path}")

if __name__ == "__main__":
    my_path = r"D:\test" 
    # 测试前 n 个零点
    test_total_time_performance(1000, save_dir=my_path)
