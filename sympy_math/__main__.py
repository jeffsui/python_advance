from sympy import Symbol,Eq, solve

# 定义一个符号变量 x
x = Symbol('x')

# 计算 x 的平方
expr = x**2
print(expr)  # Output: x**2

# 定义一个方程 x^2 - 3x + 2 = 0
eq = Eq(x**2 - 3*x + 2, 0)

# 求解方程
sol = solve(eq, x)
print(sol)  # Output: [1, 2]