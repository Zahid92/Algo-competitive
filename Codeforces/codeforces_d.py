# same differences


def f(nine):
    t = 0
    for i in range(nine):
        t += i
    return t


test = int(input())
for _ in range(test):
    n = int(input())
    a = [int(i) for i in input().split()]
    a=[a[i]-i for i in range(len(a))]
    num = 0
    d = dict()
    for item in a:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1
    for key in d.keys():
        print(key,d[key])
        num += f(d[key])

    print(num)
