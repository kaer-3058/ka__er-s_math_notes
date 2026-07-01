''' 代码语言：Python '''

import numpy

#在这里输入友矩阵或上Hessenberg形矩阵，不要忘了标记数组元素类型为float
test_matrix = numpy.array([
        [7, 4, 3, 5],
        [1, 6, 2, 14],
        [0, 5, 3, 8],
        [0, 0, 14, 2]
    ], dtype=float)

qr_matrix = test_matrix

#获取矩阵阶数(因为是方阵，所以获取行数或列数都是一样的)
n = qr_matrix.shape[0]

#使用吉文斯旋转计算R矩阵
for i in range(0,n-1):
    a = qr_matrix[i][i]
    b = qr_matrix[i+1][i]
    r = numpy.sqrt(a**2+b**2)
    c = a/r
    s = -b/r
    for j in range(i,n):
        a = qr_matrix[i][j]
        b = qr_matrix[i+1][j]
        a2 = c*a-s*b
        b2 = s*a+c*b
        qr_matrix[i][j] = a2
        qr_matrix[i+1][j] = b2

#显示R矩阵
print(qr_matrix)
