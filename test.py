def fn(y):
    y = y.copy()
    y.append(5)
    print(y)


x = [1,2,3]
print(x)
fn(x)
print(x)