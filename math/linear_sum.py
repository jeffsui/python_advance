"""
实现等比数列求和
"""
def geometric_sum(a: float, r: float, n: int) -> float:
    """
    计算等比数列的前n项和
    :param a: 首项
    :param r: 公比
    :param n: 项数
    :return: 等比数列的前n项和
    """
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)

def main():
    # 示例：计算首项为2，公比为3，前5项的和
    a = 2
    r = 3
    n = 5
    result = geometric_sum(a, r, n)
    print(f"等比数列的前{n}项和为: {result}")

if __name__ == "__main__":
    main()
# This code defines a function to calculate the sum of the first n terms of a geometric series.