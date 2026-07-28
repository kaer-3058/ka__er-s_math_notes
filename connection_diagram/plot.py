''' 绘制由纵横n个点组成的连线图 '''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

def draw_lines_fast(n, figsize=None, dpi=150):
    # 自动调整画布，避免点太挤
    base = min(max(n * 0.3, 6), 20)
    figsize = figsize or (base, base)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    # 批量构造线段数据
    segments = np.zeros((n, 2, 2))
    segments[:, 0] = np.column_stack([np.arange(1, n+1), np.zeros(n)])  # 起点
    segments[:, 1] = np.column_stack([np.zeros(n), np.arange(n, 0, -1)])  # 终点
    
    # 一次性绘制所有线段
    ax.add_collection(LineCollection(segments, colors='gray', linewidths=1))
    
    # 一次性绘制所有端点
    all_x = np.concatenate([np.arange(1, n+1), np.zeros(n)])
    all_y = np.concatenate([np.zeros(n), np.arange(n, 0, -1)])
    ax.scatter(all_x, all_y, c='steelblue', s=10, edgecolors='none')
    
    ax.set_aspect('equal')
    ax.set_xlim(-1, n+1)
    ax.set_ylim(-1, n+1)
    
    return fig, ax

#在这里输入点数n
n = 30
fig, ax = draw_lines_fast(n)
plt.show()
