# 4.3
a, b = eval(input("Please input two integer (use , to separate):\n"))

if a != b:

    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    while 1:
        c = big % small
        if c != 0:
            big = small
            small = c
            continue
        else:
            break
else:
    small = a

print("最大公约数为 {}".format(small))
print("最小公倍数为 {:d}".format(int(a * b / small)))
