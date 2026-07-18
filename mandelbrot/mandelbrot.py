import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(h, w, max_iter):
    # 定义复平面的范围 (Real 轴和 Imaginary 轴)
    y, x = np.ogrid[-1.4:1.4:h*1j, -2.0:0.8:w*1j]
    c = x + 1j*y
    z = c
    # 用于记录每个点逃逸时的迭代次数
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z * np.conj(z) > 2**2            # 判断是否发散 (半径平方大于 4)
        div_now = diverge & (divtime == max_iter)  # 找出在这一轮新发散的点
        divtime[div_now] = i                       # 记录发散时的迭代步数
        z[diverge] = 2                             # 防止发散点数值溢出

    return divtime

# 1. 生成数据 (分辨率 1000x1000，最大迭代 100 次)
mandel_img = generate_mandelbrot(1000, 1000, 100)

# 2. 绘制彩色分形图
plt.figure(figsize=(10, 10))
# cmap 可以更换为您喜欢的配色，如 'magma', 'inferno', 'plasma', 'twilight_shifted'
plt.imshow(mandel_img, cmap='twilight_shifted', extent=[-2.0, 0.8, -1.4, 1.4])
plt.axis('off')
plt.show()
