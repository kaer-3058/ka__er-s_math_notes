''' 代码语言：Python '''

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
        # find_zeta_zero(j)
        float(zetazero(j).imag)
        
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
