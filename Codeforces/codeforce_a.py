# Do not be distracted

t = int(input())
for i in range(t):
    k = int(input())
    s = input()
    c = set()
    c.add(s[0])
    f = 1
    for a in range(1, k):
        if s[a] != s[a - 1]:
           # print('aaya',s[a-1],s[a],end=" ")
            if s[a] in c:
                f = 0
                print("NO")
                break
            else:
                c.add(s[a])

    if f:
        print("YES")
