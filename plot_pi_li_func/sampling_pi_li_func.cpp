#include <iostream>
#include <fstream>
#include <cmath>
#include <primecount.hpp>

/*
    代码语言：C++
    使用本文件需要导入第三方库：primecount
    https://github.com/kimwalisch/primecount
*/

// 计算对数积分 Li(x)
double Li(double x) {
    if (x <= 1.0) {
        // x <= 1 时在实数范围内有奇点或定义域约束
        return 0.0; // 根据实际需求处理边缘情况
    }
    return std::expint(std::log(x)) - std::expint(std::log(2)); //Li(x) = li(x)-li(2)
}

int main() {
    std::ofstream outfile("data.csv");
    outfile << "x,pi,Li,ratio1,ratio2\n";

    // 按指数递增采样（方便对数横坐标）
    // 采样 3000 个点，足够保证图像平滑
    int total_points = 3000;
    double log_start = 0.47;   // 设置开始值的10的指数
    double log_end = 18;    // 设置结束值的10的指数
                            //注意上限：int_64上限约为9.223372036855*10^18

    std::cout << "正在计算 10^" << log_start << " 到 10^" << log_end << " 的数据，请稍候..." << std::endl;

    for (int i = 0; i <= total_points; ++i) {
        double exp = log_start + (log_end - log_start) * i / total_points;
        int64_t x = static_cast<int64_t>(std::pow(10.0, exp));

        if (x < 2) continue;

        // 使用 primecount 计算 pi(x)
        int64_t pi_x = primecount::pi(x);
        double li_x = Li(static_cast<double>(x));
        double ratio1 = static_cast<double>(pi_x) / li_x;               // pi(x) / Li(x)
        double ratio2 = static_cast<double>(pi_x) / (x / std::log(x));  // pi(x) / (x / ln(x))

        outfile << x << "," << pi_x << "," << li_x << "," << ratio1 << "," << ratio2 << "\n";
    }

    outfile.close();
    std::cout << "数据已成功保存至 data.csv！" << std::endl;
    return 0;
}