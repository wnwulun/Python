l1 = eval(input('请输入一个包含若干整数的列表：'))
l2 = []
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print(l2)
