############################
# python3.8 后出现的赋值表达式
# 又称为海象运算符  :=
# 可用于在内部给表达式赋值
# 例子1: 这里使用了两次len方法获取列表长度,如果数据量巨大这里重复使用将会降低性能
# numbers = [1,10,9,6,7,3,6]
# info = {
#     "length": len(numbers),
#     "sum": sum(numbers),
#     "mean": sum(numbers) / len(numbers)
# }
# print(info)
# 我们可以使用变量 先计算列表长度 和 求和 这样就可以解决这个问题
#  但是非常繁琐
# 这里使用海象运算符 就非常简单
#############################

numbers = [1,10,9,6,7,3,6]
# info = {
#     "length": n_length,
#     "sum": n_sum,
#     "mean": n_sum / n_length
# }
info = {
    "length": (n_length:=len(numbers)),
    "sum": (n_sum:=sum(numbers)),
    "mean": n_sum/n_length
}
print(info)