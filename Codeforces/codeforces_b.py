# Ordenary numbers
t = int(input())
for _ in range(t):
    n = int(input())
    digit = 0
    test = n
    num = 0
    while test:
        digit += 1
        test //= 10
   # print(digit,n)
    test = 10
    while test:
        num = 0
        test -= 1
        for i in range(digit):
            num = num * 10 + test
        if num <= n:
            break
    num = 0
    num = digit * test
    num +=( (digit - 1) * (9 - test))
    print(num)
