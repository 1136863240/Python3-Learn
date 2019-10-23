def a(b):
    if b < 3:
        a(b + 1)  # 进入递归
    else:
        print(b)

print(a(2))
