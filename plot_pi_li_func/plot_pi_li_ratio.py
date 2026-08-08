import pandas as pd
import matplotlib.pyplot as plt

# 读取 C++ 生成的数据
df = pd.read_csv('data.csv')

# 建立画布
plt.figure(figsize=(10, 6), dpi=150)

# 绘制素数定理的折线图
plt.plot(df['x'], df['ratio1'], color='#1f77b4', linewidth=1.5, label=r'$\pi(x) / \text{Li}(x)$')
plt.plot(df['x'], df['ratio2'], color="#991fb4", linewidth=1.5, label=r'$\pi(x) / (x / \ln x)$')

# 绘制 y = 1 基准红线（素数定理预测极限）
plt.axhline(y=1.0, color='r', linestyle='--', alpha=0.7, label='y = 1.0')

# 设置横坐标为对数尺度 (Logarithmic Scale)
plt.xscale('log')

# 设置 x 轴范围
plt.xlim(df['x'].min(), df['x'].max())

# 设置 y 轴范围
plt.ylim(0.8, 1.22)

# 设置图表标题和坐标轴标签
plt.title(r'Ratio of $\pi(x) / \text{Li}(x)$ and $\pi(x) / (x / \ln x)$ from $10^1$ to $10^{18}$', fontsize=14)
plt.xlabel('x (Log Scale)', fontsize=12)

# 显示网格与图例
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(fontsize=11)

# 保存图片为 PNG
plt.savefig('pi_li_ratio.png', bbox_inches='tight')
print("图像已成功保存为 pi_li_ratio.png！")

