''' 代码语言：Python '''

import numpy

#在这里输入友矩阵或上Hessenberg形矩阵，不要忘了标记数组元素类型为float
test_matrix = numpy.array([
        [0, 0, 0, -360],
        [1, 0, 0, 42],
        [0, 1, 0, 41],
        [0, 0, 1, -2]
    ], dtype=float)

#在这里输入QR迭代次数
times = 40

qr_matrix = test_matrix

#获取矩阵阶数(因为是方阵，所以获取行数或列数都是一样的)
n = qr_matrix.shape[0]

#使用吉文斯旋转简化QR迭代，全程不必进行任何显式的矩阵乘法，O(n^2)复杂度就能进行一次迭代
for t in range(0,times):
    c_list = []
    s_list = []
    for i in range(0,n-1):
        a = qr_matrix[i][i]
        b = qr_matrix[i+1][i]
        r = numpy.sqrt(a**2+b**2)
        c = a/r
        s = -b/r
        c_list.append(c)
        s_list.append(s)
        for j in range(i,n):
            a = qr_matrix[i][j]
            b = qr_matrix[i+1][j]
            a2 = c*a-s*b
            b2 = s*a+c*b
            qr_matrix[i][j] = a2
            qr_matrix[i+1][j] = b2
    for i in range(0,n-1):
        c = c_list[i]
        s = s_list[i]
        for j in range(0,i+2):
            a = qr_matrix[j][i]
            b = qr_matrix[j][i+1]
            a2 = c*a-s*b
            b2 = s*a+c*b
            qr_matrix[j][i] = a2
            qr_matrix[j][i+1] = b2

#显示迭代后的矩阵
print(qr_matrix)
